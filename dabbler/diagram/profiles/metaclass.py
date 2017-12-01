#!/usr/bin/env python

# Copyright (C) 2009-2017 Artur Wroblewski <wrobell@pld-linux.org>
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
Metaclass item for Metaclass UML metaclass :) from profiles.
"""

from __future__ import absolute_import
from dabbler.diagram.classes.klass import ClassItem
from dabbler.diagram import uml
from dabbler.UML import uml2

@uml(uml2.Component, stereotype='metaclass')
class MetaclassItem(ClassItem):
    pass

