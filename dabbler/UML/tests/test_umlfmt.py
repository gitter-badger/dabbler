#!/usr/bin/env python

# Copyright (C) 2010-2017 Arjan Molenaar <gaphor@gmail.com>
#                         Artur Wroblewski <wrobell@pld-linux.org>
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
"""
Formatting of UML model elements into text tests.
"""

from __future__ import absolute_import
import unittest

from dabbler.application import Application
from dabbler.UML.elementfactory import ElementFactory
from dabbler.UML.umlfmt import format
import dabbler.UML.uml2 as UML

factory = ElementFactory()

class AttributeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        factory.flush()


    def test_simple_format(self):
        """Test simple attribute formatting
        """
        a = factory.create(UML.Property)
        a.name = 'myattr'
        self.assertEquals('+ myattr', format(a))

        a.typeValue = 'int'
        self.assertEquals('+ myattr: int', format(a))

