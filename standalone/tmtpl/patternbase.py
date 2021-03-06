#!/usr/bin/python
#
# This file is part of the Tau Meta Tau Physica project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010, 2011, 2012  Susan Spencer and Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>..

import pysvg.builders as PYB

class pBase(object):
    """
    Base class for all pattern classes which generate SVG
    """

    # A Baseclass dictionary (list) of groups to create in the svg document, such as 'pattern' group and 'reference' group.
    groups = {}
    # A Baseclass list of ids to create in the svg document. Used to check that no duplicate id's are created.
    ids = []
    # A Baseclass list of groups that will be visible in the svg document per the user via the mkpattern commandline options.
    displayed_groups = []
    # Baseclass value for debug set manually by programmer for additional debug statements for pBase objects only.
    debug = False
    # Baseclass Dictionaries containing the styledef, markerdef, & cfg statements loaded from the styledefs.json file by the mkpattern commandline.
    styledefs = {}
    markerdefs = {}
    cfg = {}
    # Baseclass list containing the markers used in the current pattern, to create these markers in the svg document.
    markers = []


    def __init__(self):
        # Each instance of this class keeps a list of its children. Initial list is empty.
        self.children = []
        # Each instance of this class keeps a reference to its parent.  Initial value is None.
        self.parent = None

    def add(self, child):
        """
        Add a child object to parent, while setting the id
        of the child to include the 'dotted path' fo all ancestors
        """
        # Create an id for child object
        # if self is a pattern piece then it has a lettertext attribute, and the child's svg id is <self.lettertext>.<child.name>,
        if (hasattr(self, 'lettertext')):
            newid = self.lettertext + '.' + child.name
        else:
            # otherwise the child's svg id is <child.name>
            newid =  self.id + '.' + child.name

        # Check id to make sure this is not a duplicate id
        if newid in self.ids:
            raise ValueError("The name %s is used in more than one pattern object" % newid)

        # Add child id to the baseclass ids list
        self.ids.append(newid)

        child.id = newid # Set child's id value to newid string
        child.parent = self  # Set child's parent to refer to current self object

        setattr(self, child.name, child) # sets self.(child.name) to the child object, to allow referencing
        self.children.append(child) # Appends child to current self's children list

        try:
            if child.groupname not in self.groups:
                self.groups[child.groupname] = None #If group does not exist, add group name to self's group dictionary with null reference.
        except AttributeError:
            pass # don't throw an error
        return

    def mkgroupdict(self):
        """
        Return a dictionary containing keys for all the groups
        which are defined
        """
        # Creates a new dictionary that contains all the groups from the Baseclass groups dictionary.
        # This dictionary contains an empty list for each group. These lists are used in creating the SVG document.
        new_dict = {}
        for k, v in self.groups.items():
            # Add group to new dictionary & the group is now an empty list
            new_dict[k] = []
        return new_dict

    def generateText(self, x, y, label, string, styledef, trans = ''):
        """
        Generate a text element with the defined style
        """
        # in this class because it needs the styledefs
        tstyle = PYB.StyleBuilder(self.styledefs[styledef])

        svg_text = PYB.text(string, x, y)
        svg_text.set_style(tstyle.getStyle())
        svg_text.set_id(label)
        svg_text.setAttribute('transform', trans)

        return svg_text

    def getsvg(self):
        """
        Creates the svg data.
        Returns all the SVG created by this object and all its children, recursively.

        The dictionaries returned by getsvg() look like this:
        dict { groupname1 : [svgelement1, svgelement2, . . .], groupname2 : [svgelement3, svgelement4, . . .]}
        where svg elements are pySVG objects
        """

        #
        # We need to be able to have multiple groups, and have svg elements collected
        # in those groups.
        #
        # The structure of a pattern is that a document contains patterns, which contain
        # pattern pieces, which contain multiple children like paths, points, etc
        #
        # Each of these children may be in a different group.
        #
        # We need to enable a pattern piece (or any other object in the heirarchy)
        # to collect all the svg elements from their children which belong to the same
        # group as the parent, and put it inside another group with a unique ID.
        #
        # To do this, when the svg method is called for a child, it assembles a
        # dictionary which maps group names to lists of svg elements in that group.
        # If a parent element does not need to make a new group for all its children,
        # it can just pass the list up to its own parent. If an element like a pattern piece
        # needs to be in it's own group, then all the children's svg elements can be inserted
        # into a new group svg element, and only that element is in the list passed up
        # to the parent for the group that the pattern piece belongs to.
        #
        #
        svg_dict = {} # create local mydictionary
        if self.debug:
            print "getsvg() called in ", self.name
        # create empty lists for each group in the base document
        for groupname in self.groups:
            svg_dict[groupname] = [] # append groupname as an empty list

        # now recursively call getsvg() for each of my children
        for child in self.children:
            if self.debug:
                print 'Processing child ', child.name
            # If the child has a method to generate svg, call it
            if child.getsvg:
                svg_child = child.getsvg()
                # Now append everything in each group from the child to my list for that group
                for grpnm, glist in svg_child.items(): # for each group
                    for svgitem in glist:       # for each item in group
                        svg_dict[grpnm].append(svgitem) # append item to mydictionary's list for that group
        return svg_dict

    def boundingBox(self, grouplist = None):
        """
        Return two points which define a bounding box around the object
        """
        #
        # The whole bounding box calculation is flawed
        #
        # We recurse through children to get a bounding box. Only include elements
        # which are in the groups which appear in the grouplist
        #
        xlow,ylow,xhigh,yhigh = None,None,None,None
        first = 1

        if self.debug:
            print "boundingBox() called in ", self.name

        for child in self.children:
            if self.debug:
                print 'BB for child ', child.name
            if child.boundingBox:
                # if grouplist is None, use all groups
                if grouplist is None:
                    if self.debug:
                        print ' calculating bounding box for all groups'
                    grouplist = self.groups.keys()
                cxlow, cylow, cxhigh, cyhigh = child.boundingBox(grouplist)
                if child.name not in ('TitleBlock','TestGrid','info','letter'):
                    if first == 1:
                        xlow = cxlow
                        ylow = cylow
                        xhigh = cxhigh
                        yhigh = cyhigh
                        first = 0
                    elif cxlow != None:
                        if xlow != None:
                            xlow = min(xlow, cxlow)
                            ylow = min(ylow, cylow)
                            xhigh = max(xhigh, cxhigh)
                            yhigh = max(yhigh, cyhigh)
                        else:
                            xlow = cxlow
                            ylow = cylow
                            xhigh = cxhigh
                            yhigh = cyhigh

        if xlow==None:
            xlow,ylow,xhigh,yhigh=0,0,0,0
            if self.debug:
                print self.name,' xlow=None'

        return (xlow, ylow, xhigh, yhigh)

