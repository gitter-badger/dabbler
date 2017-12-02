#!/usr/bin/env python

# Copyright (C) 2008-2017 Arjan Molenaar <gaphor@gmail.com>
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
Test the backup service.
"""

from __future__ import absolute_import
from StringIO import StringIO
from dabbler.storage import storage
from dabbler.application import Application
from dabbler.misc.xmlwriter import XMLWriter
from six.moves import map

#class BackupServiceTestCase(unittest.TestCase):
class BackupServiceTestCase:

    services = ['element_factory', 'backup_service']

    def setUp(self):
        Application.init(services=self.services)
        self.element_factory = Application.get_service('element_factory')
        self.backup_service = Application.get_service('backup_service')

    def tearDown(self):
        Application.shutdown()
        
    def save_and_load(self, filename):
        factory = self.element_factory

        f = open(filename, 'r')
        storage.load(f, factory=self.element_factory)
        f.close()
        
        self.backup_service.backup()
        
        elements = list(map(factory.lookup, list(factory.keys())))

        orig = StringIO()
        storage.save(XMLWriter(orig), factory=self.element_factory)

        self.backup_service.restore()

        restored = list(map(factory.lookup, list(factory.keys())))

        assert len(elements) == len(restored)
        assert elements != restored

        copy = StringIO()
        storage.save(XMLWriter(copy), factory=self.element_factory)

        orig = orig.getvalue()
        copy = copy.getvalue()
        assert len(orig) == len(copy)
        #assert orig == copy, orig + ' != ' + copy


    def test_simple(self):
        self.save_and_load('test-diagrams/simple-items.dabbler')


    def test_namespace(self):
        self.save_and_load('test-diagrams/namespace.dabbler')

    def test_association(self):
        self.save_and_load('test-diagrams/association.dabbler')

    def test_interactions(self):
        self.save_and_load('test-diagrams/interactions.dabbler')

    def test_bicycle(self):
        self.save_and_load('test-diagrams/bicycle.dabbler')

    def test_line_align(self):
        self.save_and_load('test-diagrams/line-align.dabbler')

#    def test_gaphas_canvas(self):
#        self.save_and_load('../gaphas/dabbler-canvas.dabbler')

    def test_stereotype(self):
        self.save_and_load('test-diagrams/stereotype.dabbler')


# vim: sw=4:et:ai
