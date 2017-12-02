#!/usr/bin/env python

# Copyright (C) 2009-2017 Arjan Molenaar <gaphor@gmail.com>
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
Test GitHub issue #4. Diagram could not be loaded due to JuggleError
(presumed cyclic resolving of diagram items).
"""

from __future__ import absolute_import

from dabbler.storage.storage import load
from dabbler.tests import TestCase


class CyclicDiagramTestCase(TestCase):
    # services = TestCase.services + ['undo_manager']

    def setUp(self):
        super(CyclicDiagramTestCase, self).setUp()

    def test_bug(self):
        """
        Load file.

        This does not nearly resemble the error, since the model should
        be loaded from within the mainloop (which will delay all updates).
        """
        load('test-diagrams/diagram-#4.dabbler', self.element_factory)

    def test_bug_idle(self):
        """
        Load file in gtk main loop.

        This does not nearly resemble the error, since the model should
        be loaded from within the mainloop (which will delay all updates).
        """
        import gobject, gtk
        def handler():
            try:
                load('test-diagrams/diagram-#4.dabbler', self.element_factory)
            finally:
                gtk.main_quit()

        assert gobject.timeout_add(1, handler) > 0
        gtk.main()

# vi:sw=4:et:ai
