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
"""
Unit tests for simple items.
"""

from __future__ import absolute_import
from dabbler.tests import TestCase
from dabbler.diagram.simpleitem import Line, Box, Ellipse
from gaphas import View


class SimpleItemTestCase(TestCase):

    def setUp(self):
        super(SimpleItemTestCase, self).setUp()
        self.view = View(self.diagram.canvas)

    def test_line(self):
        """
        """
        self.diagram.create(Line)
        
    def test_box(self):
        """
        """
        self.diagram.create(Line)

    def test_ellipse(self):
        """
        """
        self.diagram.create(Ellipse)


# vim:sw=4:et:ai
