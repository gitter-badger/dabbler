#!/usr/bin/env python

# Copyright (C) 2007-2017 Arjan Molenaar <gaphor@gmail.com>
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
from dabbler.ui.consolewindow import ConsoleWindow
from dabbler.tests.testcase import TestCase

class ConsoleWindowTestCase(TestCase):

    services = TestCase.services + ['main_window', 'ui_manager', 'action_manager', 'properties']

    def test1(self):
        import gtk
        window = ConsoleWindow()
        assert len(window.action_group.list_actions()) == 2, window.action_group.list_actions()
        window.open()
        window.close()

