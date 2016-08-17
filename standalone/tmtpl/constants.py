#!/usr/bin/python
#
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010, 2011, 2012 Susan Spencer and Steve Conklin
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from math import pi

def angleOfDegree(degree):
    return degree * pi/180.0

# angle constants
ANGLE0 = angleOfDegree(0)
ANGLE30 = angleOfDegree(30)
ANGLE45 = angleOfDegree(45)
ANGLE60 = angleOfDegree(60)
ANGLE90 = angleOfDegree(90)
ANGLE135 = angleOfDegree(135)
ANGLE180 = angleOfDegree(180)
ANGLE225 = angleOfDegree(225)
ANGLE270 = angleOfDegree(270)
ANGLE315 = angleOfDegree(315)
# measurement constants

IN_TO_CM = (2.54/1.0) #convert inches to centimeters
CM_TO_IN = (1/2.54) #convert centimeters to inches

IN_TO_PT = (72.72/1.0) #convert inches to printer's points
CM_TO_PT = (72.72/2.54) #convert centimeters to printer's points
PT_TO_IN = (1/IN_TO_PT)
PT_TO_CM = (1/CM_TO_PT)

IN_TO_PX = (90/1.0) #convert inches to pixels - Inkscape value
CM_TO_PX = (90/2.54) #convert cm to px - Inkscape value
MM_TO_PX=CM_TO_PX/10.0 # convert mm to px - Inkscape value
CM = CM_TO_PX # shorthand for CM_TO_PX, useful in design file
IN = IN_TO_PX # shorthand for IN_TO_PX, useful in design file
MM = MM_TO_PX # need millimeters shorthand, too!

PX_TO_IN = (1/IN_TO_PX) # convert pixels to inches - Inkscape value 90ppi
PX_TO_CM = (1/CM_TO_PX) # convert pixels to centimeters - Inkscape
PX_TO_MM = (1/MM_TO_PX) # convert pixels to millimeters - inkscape



# sewing constants
QUARTER_SEAM_ALLOWANCE = (IN_TO_PX*1/4.0) #1/4" seam allowance
SEAM_ALLOWANCE = (IN_TO_PX*5/8.0) #5/8" seam allowance
HEM_ALLOWANCE = (IN_TO_PX*2.0) #2" seam allowance
PATTERN_OFFSET = (SEAM_ALLOWANCE*3.0) #1-7/8" between patterns
