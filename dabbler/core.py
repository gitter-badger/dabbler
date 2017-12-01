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
The Core module provides an entry point for Dabbler's core constructs.

An average module should only need to import this module.
"""

from __future__ import absolute_import
from dabbler.application import inject, Application
from dabbler.transaction import Transaction, transactional
from dabbler.action import action, toggle_action, radio_action, open_action, build_action_group
from dabbler.i18n import _

# vim:sw=4:et:ai
