#!/usr/bin/env python

# Copyright (C) 2002-2017 Adam Boduch <adam.boduch@gmail.com>
#                         Arjan Molenaar <gaphor@gmail.com>
#                         Artur Wroblewski <wrobell@pld-linux.org>
#                         Dan Yeaw <dan@yeaw.me>
#                         syt <noreply@example.com>
#
# This file is part of Gaphor.
#
# Gaphor is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# Gaphor is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaphor.  If not, see <http://www.gnu.org/licenses/>.
"""This module contains a model element Diagram which is the abstract
representation of a UML diagram. Diagrams can be visualized and edited.

The DiagramItemContainer class extends the gaphas.ItemContainer class."""

from __future__ import absolute_import

import uuid

import gaphas
from six.moves import filter

from gaphor.UML.uml2 import Namespace, PackageableElement


class DiagramItemContainer(gaphas.ItemContainer):
    """DiagramItemContainer extends the gaphas.ItemContainer class.  Updates to the item_container
    can be blocked by setting the block_updates property to true.  A save
    function can be applied to all root item_container items.  ItemContainer items can be
    selected with an optional expression filter."""

    def __init__(self, diagram):
        """Initialize the diagram item_container with the supplied diagram.  By default,
        updates are not blocked."""

        super(DiagramItemContainer, self).__init__()
        self._diagram = diagram
        self._block_updates = False

    diagram = property(lambda s: s._diagram)

    def _set_block_updates(self, block):
        """Sets the block_updates property.  If false, the diagram item_container is
        updated immediately."""

        self._block_updates = block
        if not block:
            self.update_now()

    block_updates = property(lambda s: s._block_updates, _set_block_updates)

    def update_now(self):
        """Update the diagram item_container, unless block_updates is true."""

        if self._block_updates:
            return
        super(DiagramItemContainer, self).update_now()

    def save(self, save_func):
        """Apply the supplied save function to all root diagram items."""

        for item in self.get_root_items():
            save_func(None, item)

    def postload(self):
        """Called after the diagram item_container has loaded.  Currently does nothing.
        """
        pass

    def select(self, expression=lambda e: True):
        """Return a list of all item_container items that match expression."""

        return list(filter(expression, self.get_all_items()))


class Diagram(Namespace, PackageableElement):
    """Diagrams may contain model elements and can be owned by a Package.
    A diagram is a Namespace and a PackageableElement."""

    def __init__(self, id=None, factory=None):
        """Initialize the diagram with an optional id and element factory.
        The diagram also has a item_container."""

        super(Diagram, self).__init__(id, factory)
        self.item_container = DiagramItemContainer(self)

    def save(self, save_func):
        """Apply the supplied save function to this diagram and the item_container."""

        super(Diagram, self).save(save_func)
        save_func('item_container', self.item_container)

    def postload(self):
        """Handle post-load functionality for the diagram item_container."""
        super(Diagram, self).postload()
        self.item_container.postload()

    def create(self, type, parent=None, subject=None):
        """Create a new item_container item on the item_container. It is created with
        a unique ID and it is attached to the diagram's root item.  The type
        parameter is the element class to create.  The new element also has an
        optional parent and subject."""

        assert issubclass(type, gaphas.Item)
        obj = type(str(uuid.uuid1()))
        if subject:
            obj.subject = subject
        self.item_container.add(obj, parent)
        return obj

    def unlink(self):
        """Unlink all item_container items then unlink this diagram."""

        for item in self.item_container.get_all_items():
            try:
                item.unlink()
            except:
                pass

        super(Diagram, self).unlink()
