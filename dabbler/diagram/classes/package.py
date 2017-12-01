#!/usr/bin/env python

# Copyright (C) 2002-2017 Arjan Molenaar <gaphor@gmail.com>
#                         Artur Wroblewski <wrobell@pld-linux.org>
#                         Dan Yeaw <dan@yeaw.me>
#                         syt <noreply@example.com>
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
Package diagram item.
"""

from __future__ import absolute_import
from dabbler.UML import uml2
from dabbler.diagram.nameditem import NamedItem


class PackageItem(NamedItem):

    __uml__ = uml2.Package, uml2.Profile
    __stereotype__ = {
        'profile': uml2.Profile,
    }
    __style__ = {
        'min-size': (NamedItem.style.min_size[0], 70),
        'name-font': 'sans bold 10',
        'name-padding': (25, 10, 5, 10),
        'tab-x': 50,
        'tab-y': 20,
    }

    def __init__(self, id=None):
        super(PackageItem, self).__init__(id)


    def draw(self, context):
        super(PackageItem, self).draw(context)

        cr = context.cairo
        o = 0.0
        h = self.height
        w = self.width
        x = self.style.tab_x
        y = self.style.tab_y
        cr.move_to(x, y)
        cr.line_to(x, o)
        cr.line_to(o, o)
        cr.line_to(o, h)
        cr.line_to(w, h)
        cr.line_to(w, y)
        cr.line_to(o, y)
        cr.stroke()


# vim:sw=4:et
