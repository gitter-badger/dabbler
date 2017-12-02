#!/usr/bin/env python

# Copyright (C) 2005-2017 Arjan Molenaar <gaphor@gmail.com>
#                         Dan Yeaw <dan@yeaw.me>
#                         slmm <noreply@example.com>
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
from .interfaces import *

class DiagramTabChange(object):

    interface.implements(IDiagramTabChange)
    
    def __init__(self, item):
        self.item = item
        self.diagram_tab = item.diagram_tab


class DiagramSelectionChange(object):

    interface.implements(IDiagramSelectionChange)
    
    def __init__(self, diagram_view, focused_item, selected_items):
        self.diagram_view = diagram_view
        self.focused_item = focused_item
        self.selected_items = selected_items


# vim:sw=4:et:ai
