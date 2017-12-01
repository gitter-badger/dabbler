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
from __future__ import print_function
import unittest

class ActionManagerTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLoadAll(self):
        from dabbler.application import Application
        Application.init()
        am = Application.get_service('action_manager')
        ui = am.ui_manager.get_ui()
        print(ui)
