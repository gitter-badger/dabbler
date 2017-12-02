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
Implementation of interface.
"""

from __future__ import absolute_import
from dabbler.UML import uml2
from dabbler.diagram.diagramline import DiagramLine

class ImplementationItem(DiagramLine):

    __uml__          = uml2.Implementation

    def __init__(self, id = None):
        DiagramLine.__init__(self, id)
        self._solid = False 


    def draw_head(self, context):
        cr = context.cairo
        cr.move_to(0, 0)
        if not self._solid:
            cr.set_dash((), 0)
            cr.line_to(15, -10)
            cr.line_to(15, 10)
            cr.close_path()
            cr.stroke()
            cr.move_to(15, 0)


    def draw(self, context):
        if not self._solid:
            context.cairo.set_dash((7.0, 5.0), 0)
        super(ImplementationItem, self).draw(context)



# vim:sw=4
