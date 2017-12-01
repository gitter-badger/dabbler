#!/usr/bin/env python

# Copyright (C) 2007-2017 Arjan Molenaar <gaphor@gmail.com>
#                         Artur Wroblewski <wrobell@pld-linux.org>
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
All Item's defined in the diagram package. This module
is a shorthand for importing each module individually.
"""

# Base classes:
from __future__ import absolute_import
from dabbler.diagram.diagramitem import DiagramItem
from dabbler.diagram.diagramline import DiagramLine, NamedLine
from dabbler.diagram.elementitem import ElementItem
from dabbler.diagram.nameditem import NamedItem
from dabbler.diagram.compartment import CompartmentItem, FeatureItem
from dabbler.diagram.classifier import ClassifierItem

# General:
from dabbler.diagram.comment import CommentItem
from dabbler.diagram.commentline import CommentLineItem
from dabbler.diagram.simpleitem import Line, Box, Ellipse

# Classes:
from dabbler.diagram.classes.klass import ClassItem, OperationItem
from dabbler.diagram.classes.interface import InterfaceItem
from dabbler.diagram.classes.package import PackageItem
from dabbler.diagram.classes.association import AssociationItem
from dabbler.diagram.classes.dependency import DependencyItem
from dabbler.diagram.classes.generalization import GeneralizationItem
from dabbler.diagram.classes.implementation import ImplementationItem

# Components:
from dabbler.diagram.artifact import ArtifactItem
from dabbler.diagram.connector import ConnectorItem
from dabbler.diagram.component import ComponentItem
from dabbler.diagram.node import NodeItem
from dabbler.diagram.components.subsystem import SubsystemItem

# Actions:
from dabbler.diagram.activitynodes import ActivityNodeItem
from dabbler.diagram.activitynodes import InitialNodeItem, ActivityFinalNodeItem
from dabbler.diagram.activitynodes import FlowFinalNodeItem
from dabbler.diagram.activitynodes import DecisionNodeItem
from dabbler.diagram.activitynodes import ForkNodeItem
from dabbler.diagram.objectnode import ObjectNodeItem
from dabbler.diagram.actions.action import ActionItem, SendSignalActionItem, AcceptEventActionItem
from dabbler.diagram.actions.flow import FlowItem
from dabbler.diagram.actions.partition import PartitionItem

# Interactions
from dabbler.diagram.interaction import InteractionItem
from dabbler.diagram.lifeline import LifelineItem
from dabbler.diagram.message import MessageItem

# States
from dabbler.diagram.states import VertexItem
from dabbler.diagram.states.state import StateItem
from dabbler.diagram.states.transition import TransitionItem
from dabbler.diagram.states.finalstate import FinalStateItem
from dabbler.diagram.states.pseudostates import InitialPseudostateItem, HistoryPseudostateItem

# Use Cases:
from dabbler.diagram.actor import ActorItem
from dabbler.diagram.usecase import UseCaseItem
from dabbler.diagram.include import IncludeItem
from dabbler.diagram.extend import ExtendItem

# Stereotypes:
from dabbler.diagram.extension import ExtensionItem
from dabbler.diagram.profiles.metaclass import MetaclassItem

