#!/usr/bin/env python

# Copyright (C) 2001-2017 Adam Boduch <adam.boduch@gmail.com>
#                         Arjan Molenaar <gaphor@gmail.com>
#                         Dan Yeaw <dan@yeaw.me>
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
"""
This module contains user interface related code, such as the
main screen and diagram windows.
"""

from __future__ import absolute_import
import os
from os import path

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gaphor.misc import get_user_data_dir


def _get_accel_map_filename():
    """
    The Gaphor accelMap file ($HOME/.gaphor/accelmap).
    """
    
    user_data_dir = get_user_data_dir()
    
    if not path.exists(user_data_dir):
        os.mkdir(user_data_dir)
    return path.join(user_data_dir, 'accelmap')


def load_accel_map():
    """
    Load the user accelerator map from the gaphor user home directory
    """
    filename = _get_accel_map_filename()
    if path.exists(filename) and path.isfile(filename):
        Gtk.AccelMap.load(filename)


def save_accel_map():
    """
    Save the contents of the GtkAccelMap to a file.
    """
    filename = _get_accel_map_filename()
    Gtk.AccelMap.save(filename)   


# vim:sw=4:et:
