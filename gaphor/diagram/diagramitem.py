# vim:sw=4:et
"""DiagramItem provides basic functionality for presentations.
Such as a modifier 'subject' property and a unique id.
"""

import gobject
import diacanvas
from diacanvas import CanvasItem

from gaphor import resource
from gaphor.UML import Element, Presentation
from gaphor.UML.properties import association


class DiagramItem(Presentation):
    """Basic functionality for all model elements (lines and elements!).

    This class contains common functionallity for model elements and
    relationships.
    It provides an interface similar to UML.Element for connecting and
    disconnecting signals.

    This class is not very useful on its own. It contains some glue-code for
    diacanvas.DiaCanvasItem and gaphor.UML.Element.

    Example:
        class ElementItem(diacanvas.CanvasElement, DiagramItem):
            connect = DiagramItem.connect
            disconnect = DiagramItem.disconnect
            ...
    """
    __gproperties__ = {
        'subject':        (gobject.TYPE_PYOBJECT, 'subject',
                         'subject held by the diagram item',
                         gobject.PARAM_READWRITE),
    }

    __gsignals__ = {
        '__unlink__': (gobject.SIGNAL_RUN_FIRST,
                       gobject.TYPE_NONE, (gobject.TYPE_STRING,))
    }

    popup_menu = ()

    def __init__(self, id=None):
        Presentation.__init__(self)
        self._id = id # or uniqueid.generate_id()

        # Mapping to convert handlers to GObject signal ids.
        self.__handler_to_id = { }

        # Add the class' on_subject_notify() as handler:
        self.connect('notify::subject', type(self).on_subject_notify)

        # __the_subject is a backup that is used to disconnect signals when a
        # new subject is set (or the original one is removed)
        self.__the_subject = None

        # properties, which should be saved in file
        self._persistent_props = set()


    id = property(lambda self: self._id, doc='Id')

    def set_prop_persistent(self, name):
        """
        Specify property of diagram item, which should be saved in file.
        """
        self._persistent_props.add(name)


    def do_set_property(self, pspec, value):
        if pspec.name == 'subject':
            self.set_subject(value)
        else:
            raise AttributeError, 'Unknown property %s' % pspec.name


    def do_get_property(self, pspec):
        if pspec.name == 'subject':
            return self.subject
        else:
            raise AttributeError, 'Unknown property %s' % pspec.name


    # UML.Element interface used by properties:

    # TODO: Use adapters for load/save functionality
    def save(self, save_func):
        if self.subject:
            save_func('subject', self.subject)

        # save persistent properties
        for p in self._persistent_props:
            save_func(p, getattr(self.props, p))


    def load(self, name, value):
        if name == 'subject':
            #print 'loading subject', value
            type(self).subject.load(self, value)
        else:
            #log.debug('Setting unknown property "%s" -> "%s"' % (name, value))
            try:
                self.set_property(name, eval(value))
            except:
                log.warning('%s has no property named %s (value %s)' % (self, name, value))

    def postload(self):
        if self.subject:
            self.on_subject_notify(type(self).subject)

    # TODO: remove, use signaling from gaphor.UML.Element
    def unlink(self):
        """Send the unlink signal and remove itself from the canvas.
        """
        #log.debug('DiagramItem.unlink(%s)' % self)
        # emit the __unlink__ signal the way UML.Element would have done:
        self.set_subject(None)

        self.emit('__unlink__', '__unlink__')


        self.set_property('parent', None)

    # gaphor.UML.Element like signal interface:

    # TODO: remove, use signaling from gaphor.UML.Element
    def connect(self, name, handler, *args):
        """Connect a handler to signal name with args.
        Note that in order to connect to the subject property, you have
        to use "notify::subject".
        A signal handler id is returned.
        """
        id = CanvasItem.connect(self, name, handler, *args)
        key = (handler,) + args
        try:
            self.__handler_to_id[key].append(id)
        except:
            # it's a new entry:
            self.__handler_to_id[key] = [id]
        return id

    # TODO: remove, use signaling from gaphor.UML.Element
    def disconnect(self, handler_or_id, *args):
        """Disconnect a signal handler. If handler_or_id is an integer (int)
        it is expected to be the signal handler id. Otherwise
        handler_or_id + *args are the same arguments passed to the connect()
        method (except the signal name). The latter form is used by
        gaphor.UML.Element.
        """
        if isinstance(handler_or_id, int):
            CanvasItem.disconnect(self, handler_or_id)
            for v in self.__handler_to_id.itervalues():
                if handler_or_id in v:
                    v.remove(handler_or_id)
                    break
        else:
            try:
                key = (handler_or_id,) + args
                ids = self.__handler_to_id[key]
            except KeyError, e:
                log.error("Couldn't retrieve connection handle ids", e)
            else:
                for id in ids:
                    CanvasItem.disconnect(self, id)
                del self.__handler_to_id[key]

    def notify(self, name, pspec=None):
        CanvasItem.notify(self, name)

    def save_property(self, save_func, name):
        """Save a property, this is a shorthand method.
        """
        save_func(name, self.get_property(name))

    def save_properties(self, save_func, *names):
        """Save a property, this is a shorthand method.
        """
        for name in names:
            self.save_property(save_func, name)

    def set_subject(self, subject=None):
        """Set the subject. In addition, if there are no more presentations
        on the subject, the subject is unlink()'ed.
        """
        #log.debug('set_subject %s %s' % (self.subject, subject))
        old = self.subject

        # remove the subject if we have one
        if self.subject:
            del self.subject

        if old and len(old.presentation) == 0:
            #log.debug('diagramitem.unlink: No more presentations: unlinking')
            old.unlink()
         
        self.subject = subject

    def get_popup_menu(self):
        return self.popup_menu

    def _subject_connect_helper(self, element, callback_prefix, prop_list):
        """Connect a signal notifier. The notifier can be just the name of
        one of the subjects properties.

        See: DiagramItem.on_subject_notify()
        """
        #log.debug('_subject_connect_helper: %s %s %s' % (element, callback_prefix, prop_list))

        prop = prop_list[0]
        callback_name = '%s_%s' % (callback_prefix, prop)
        if len(prop_list) == 1:
            #log.debug('_subject_connect_helper - %s %s' % (element, callback_name))
            handler = getattr(self, callback_name)
            element.connect(prop, handler)
            # Call the handler, so it can update its state
            #handler(prop, getattr(type(element), prop))
            #handler(element, getattr(type(element), prop))
        else:
            p = getattr(element, prop)
            #log.debug('_subject_connect_helper 2 - %s: %s' % (prop, p))
            pl = prop_list[1:]
            element.connect(prop, self._on_subject_notify_helper, callback_name, pl, [p])
            if p:
                self._subject_connect_helper(p, callback_name, pl)
            else:
                pass

    def _subject_disconnect_helper(self, element, callback_prefix, prop_list):
        """Disconnect a previously connected signal handler.

        See: DiagramItem.on_subject_notify()
        """
        #log.debug('_subject_disconnect_helper: %s %s %s' % (element, callback_prefix, prop_list))
        prop = prop_list[0]
        callback_name = '%s_%s' % (callback_prefix, prop)
        if len(prop_list) == 1:
            #log.debug('_subject_disconnect_helper - %s %s' % (element, callback_name))
            handler = getattr(self, callback_name)
            element.disconnect(handler)
            # Call the handler, so it can update its state
            #handler(element, getattr(type(element), prop))
        else:
            p = getattr(element, prop)
            #log.debug('_subject_disconnect_helper 2 - %s' % prop)
            pl = prop_list[1:]
            element.disconnect(self._on_subject_notify_helper, callback_name, pl, [p])
            if p:
                self._subject_disconnect_helper(p, callback_name, pl)
            else:
                pass

    def _on_subject_notify_helper(self, element, pspec, callback_name, prop_list, old):
        """This signal handler handles signals that are not direct properties
        of self.subject (e.g. 'subject.lowerValue.value'). This way the
        presentation class is not bothered with the details of keeping track
        of those properties.

        NOTE: This only works for properties with multiplicity [0..1] or [1].

        See: DiagramItem.on_subject_notify()
        """
        name = pspec.name
        prop = getattr(element, name)
        #log.debug('_on_subject_notify_helper: %s %s %s %s %s' % (element, name, callback_name, prop_list, old))
        # Attach a new signal handler with the new 'old' value:
        if old[0]:
            #log.info('disconnecting')
            self._subject_disconnect_helper(old[0], callback_name, prop_list)
        if prop:
            self._subject_connect_helper(prop, callback_name, prop_list)

        # Set the new "old" value
        old[0] = prop

    def on_subject_notify(self, pspec, notifiers=()):
        """A new subject is set on this model element.
        notifiers is an optional tuple of elements that also need a
        callback function. Callbacks have the signature
        on_subject_notify__<notifier>(self, subject, pspec).

        A notifier can be a property of subject (e.g. 'name') or a property
        of a property of subject (e.g. 'lowerValue.value').
        """
        #log.info('DiagramItem.on_subject_notify: %s' % self.__subject_notifier_ids)
        # First, split all notifiers on '.'
        callback_prefix = 'on_subject_notify_'
        notifiers = map(str.split, notifiers, ['.'] * len(notifiers))
        old_subject = self.__the_subject
        subject_connect_helper = self._subject_connect_helper
        subject_disconnect_helper = self._subject_disconnect_helper

        if old_subject:
            for n in notifiers:
                #self._subject_disconnect(self.__the_subject, n)
                subject_disconnect_helper(old_subject, callback_prefix, n)

        if self.subject:
            subject = self.__the_subject = self.subject
            for n in notifiers:
                #log.debug('DiaCanvasItem.on_subject_notify: %s' % signal)
                #self._subject_connect(self.subject, n)
                subject_connect_helper(subject, callback_prefix, n)

        # Execute some sort of ItemNewSubject action
        try:
            main_window = resource('MainWindow')
        except KeyError:
            pass
        else:
            main_window.execute_action('ItemNewSubject')
        self.request_update()

    # DiaCanvasItem callbacks

    # TODO: use connectable adapter here.
    def _on_glue(self, handle, wx, wy, parent_class):
        """This function is used to notify the connecting item
        about being connected. handle.owner.allow_connect_handle() is
        called to determine if a connection is allowed.
        """
        if handle.owner.allow_connect_handle(handle, self):
            #print self.__class__.__name__, 'Glueing allowed.'
            return parent_class.on_glue(self, handle, wx, wy)
        #else:
            #print self.__class__.__name__, 'Glueing NOT allowed.'
        # Dummy value with large distance value
        return 10000.0, (0, 0)

    def _on_connect_handle(self, handle, parent_class):
        """This function is used to notify the connecting item
        about being connected. handle.owner.allow_connect_handle() is
        called to determine if a connection is allowed. If the connection
        succeeded handle.owner.confirm_connect_handle() is called.
        """
        if handle.owner.allow_connect_handle(handle, self):
            #print self.__class__.__name__, 'Connection allowed.'
            ret = parent_class.on_connect_handle(self, handle)
            if ret != 0:
                handle.owner.confirm_connect_handle(handle)
                return ret
        #else:
            #print self.__class__.__name__, 'Connection NOT allowed.'
        return 0

    def _on_disconnect_handle(self, handle, parent_class):
        """Use this function to disconnect handles. It notifies
        the connected item about being disconnected.
        handle.owner.allow_disconnect_handle() is
        called to determine if a connection is allowed to be removed.
        If the disconnect succeeded handle.owner.confirm_connect_handle()
        is called.
        """
        if handle.owner.allow_disconnect_handle(handle):
            #print self.__class__.__name__, 'Disconnecting allowed.'
            ret = parent_class.on_disconnect_handle(self, handle)
            if ret != 0:
                handle.owner.confirm_disconnect_handle(handle, self)
                # TODO: call ConnectAction
                return ret
        #else:
            #print self.__class__.__name__, 'Disconnecting NOT allowed.'
        return 0
