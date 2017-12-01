#!/usr/bin/env python

# Copyright (C) 2009-2017 Arjan Molenaar <gaphor@gmail.com>
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
from __future__ import absolute_import

from dabbler.UML import uml2, umllex
from dabbler.diagram.classes.klass import ClassItem
from dabbler.diagram.compartment import FeatureItem
from dabbler.tests.testcase import TestCase


class FeatureTestCase(TestCase):
    def setUp(self):
        super(FeatureTestCase, self).setUp()

    def tearDown(self):
        super(FeatureTestCase, self).tearDown()

    def testAttribute(self):
        """
        Test how attribute is updated
        """
        attr = self.element_factory.create(uml2.Property)
        umllex.parse(attr, '-name:myType')

        clazzitem = self.create(ClassItem, uml2.Class)
        clazzitem.subject.ownedAttribute = attr
        self.assertEquals(1, len(clazzitem._compartments[0]))

        item = clazzitem._compartments[0][0]
        self.assertTrue(isinstance(item, FeatureItem))

        size = item.get_size()
        self.assertNotEquals((0, 0), size)

        attr.defaultValue = 'myDefault'

        self.diagram.canvas.update()
        self.assertTrue(size < item.get_size())

# vim:sw=4:et:ai
