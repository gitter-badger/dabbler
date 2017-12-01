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
from __future__ import absolute_import
from zope import interface
from dabbler.UML.uml2 import Element
from dabbler.interfaces import IService
from dabbler.core import inject

# Register application specific picklers:
from dabbler.misc.latepickle import LatePickler


import pickle
from six.moves import map
class MyPickler(LatePickler):
    """
    Customize the pickler to only delay instantiations of Element objects.
    """

    def delay(self, obj):
        return isinstance(obj, Element)


class BackupService(object):
    """
    This service makes backups every *x* minutes.
    """

    interface.implements(IService)

    element_factory = inject('element_factory')

    def __init__(self):
        self.tempname = '.backup.dabbler.tmp'


    def init(self, app):
        pass


    def shutdown(self):
        pass


    def backup(self):
        f = open(self.tempname, 'w')
        try:
            pickler = MyPickler(f)
            pickler.dump(self.element_factory.lselect())
        finally:
            f.close()


    def restore(self):
        f = open(self.tempname, 'r')
        try:
            elements = pickle.Unpickler(f).load()
        finally:
            f.close()
        self.element_factory.flush()
        list(map(self.element_factory.bind, elements))


# vim: sw=4:et:ai
