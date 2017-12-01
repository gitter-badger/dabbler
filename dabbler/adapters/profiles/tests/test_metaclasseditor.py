#!/usr/bin/env python

# Copyright (C) 2010-2017 Arjan Molenaar <gaphor@gmail.com>
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
from dabbler.tests import TestCase
from dabbler.adapters.profiles.metaclasseditor import MetaclassNameEditor
from dabbler.diagram import items
from dabbler.UML import uml2
import gtk

class MetaclassEditorTest(TestCase):

    def test_name_selection(self):
        ci = self.create(items.MetaclassItem, uml2.Class)
        ci.subject.name = 'Class'
        editor = MetaclassNameEditor(ci)
        page = editor.construct()
        self.assertTrue(page)
        combo = page.get_children()[0].get_children()[1]
        self.assertSame(gtk.ComboBoxEntry, type(combo))

        self.assertEquals("Class", combo.child.get_text())

        ci.subject.name = 'Blah'
        self.assertEquals('Blah', combo.child.get_text())


# vim:sw=4:et:ai
