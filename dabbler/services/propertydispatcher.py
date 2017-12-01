#!/usr/bin/env python

# Copyright (C) 2009-2017 Adam Boduch <adam.boduch@gmail.com>
#                         Arjan Molenaar <gaphor@gmail.com>
#                         Dan Yeaw <dan@yeaw.me>
#
# This file is part of Dabbler.
#
# Dabbler is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# Dabbler is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Dabbler.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import
from zope import interface, component

from logging import getLogger
from dabbler.core import inject
from dabbler.interfaces import IService
from dabbler.UML.interfaces import IElementChangeEvent


class PropertyDispatcher(object):
    """
    The Propery Dispatcher allows classes to register on events originated
    by a specific element property, instead of the event type.

    This makes it easier for (for example) items to register on events from
    a specific class, rather than just AssociationChangeEvents, which could
    originate on a whole lot of classes.
    """

    interface.implements(IService)
    logger = getLogger('PropertyDispatcher')

    component_registry = inject('component_registry')

    def __init__(self):
        # Handlers is a dict of sets
        self._handlers = {}

    def init(self, app):
        
        self.logger.info('Starting')
        
        self.component_registry.register_handler(self.on_element_change_event)

    def shutdown(self):
        
        self.logger.info('Shutting down')
        
        self.component_registry.unregister_handler(self.on_element_change_event)

    def register_handler(self, property, handler, exact=False):
        
        self.logger.info('Registring handler')
        self.logger.debug('Property is %s' % property)
        self.logger.debug('Handler is %s' % handler)
        
        try:
            self._handlers[property].add(handler)
        except KeyError:
            self._handlers[property] = set([handler])

    def unregister_handler(self, property, handler):
        
        self.logger.info('Unregistering handler')
        self.logger.debug('Property is %s' % property)
        self.logger.debug('Handler is %s' % handler)
        
        s = self._handlers.get(property)
        if s:
            s.discard(handler)

    @component.adapter(IElementChangeEvent)
    def on_element_change_event(self, event):
        
        self.logger.info('Handling IElementChangeEvent')
        
        property = event.property
        
        self.logger.debug('Property is %s' % property)

        s = self._handlers.get(property)
        if not s:
            return
        for handler in s:
            try:
                handler(event)
            except Exception as e:
                log.error('problem executing handler %s' % handler, exc_info=True)


# vim:sw=4:et:ai
