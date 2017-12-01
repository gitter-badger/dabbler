#!/usr/bin/env python

# Copyright (C) 2004-2017 Adam Boduch <adam.boduch@gmail.com>
#                         Arjan Molenaar <gaphor@gmail.com>
#                         Dan Yeaw <dan@yeaw.me>
#                         slmm <noreply@example.com>
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
"""
This plugin extends Dabbler with XMI export functionality.
"""

from __future__ import absolute_import
import gtk
from zope import interface, component
from dabbler.core import _, inject, action, build_action_group
from dabbler.interfaces import IService, IActionProvider
from dabbler.ui.filedialog import FileDialog

from . import exportmodel

class XMIExport(object):

    interface.implements(IService, IActionProvider)

    element_factory = inject('element_factory')
    main_window = inject('main_window')

    menu_xml = """
      <ui>
        <menubar action="mainwindow">
          <menu action="file">
            <menu action="file-export">
              <menuitem action="file-export-xmi" />
            </menu>
          </menu>
        </menubar>
      </ui>"""
    
    def __init__(self):
        self.action_group = build_action_group(self)

    def init(self, app):
        pass

    def shutdown(self):
        pass

    @action(name='file-export-xmi', label=_('Export to XMI'),
            tooltip=_('Export model to XMI (XML Model Interchange) format'))
    def execute(self):
        filename = self.main_window.get_filename()
        if filename:
            filename = filename.replace('.dabbler', '.xmi')
        else:
            filename = 'model.xmi'

        file_dialog = FileDialog(_('Export model to XMI file'),\
                                 action='save',\
                                 filename=filename)
        
        filename = file_dialog.selection
        
        if filename and len(filename) > 0:
            log.debug('Exporting XMI model to: %s' % filename)
            export = exportmodel.XMIExport(self.element_factory)
            try:
                export.export(filename)
            except Exception as e:
                log.error('Error while saving model to file %s: %s' % (filename, e))


# vim:sw=4:et
