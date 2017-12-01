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
Test transitions.
"""

from __future__ import absolute_import
from dabbler.UML import uml2
from dabbler.diagram.states.transition import TransitionItem
from dabbler.tests.testcase import TestCase

class TransitionTestCase(TestCase):
    """
    Test the working of transitions
    """

    def test_transition_guard(self):
        """Test events of transition.guard.
        """
        item = self.create(TransitionItem, uml2.Transition)
        assert item._guard.text == ''

        c = self.element_factory.create(uml2.Constraint)
        c.specification = 'blah'
        assert item._guard.text == ''

        item.subject.guard = c
        assert item.subject.guard is c
        assert item._guard.text == 'blah', item._guard.text

        del c.specification
        assert item._guard.text == '', item._guard.text

        c.specification = 'foo'
        assert item._guard.text == 'foo', item._guard.text

# vim:sw=4:et:ai
