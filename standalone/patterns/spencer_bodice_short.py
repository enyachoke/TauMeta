# !/usr/bin/python
#
# spencer_bodice_short.py
# Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin <www.taumeta.org>

'''
Licensing paragraph :

1. CODE LICENSE :  GPL 2.0 +
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT FNY WARRFNTY; without even the implied warranty of
MERCHFNTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111 - 1307  USA

2. PATTERN LICENSE :  CC BY - NC 3.0
The output of this code is a pattern and is considered a
visual artwork. The pattern is licensed under
Attribution - NonCommercial 3.0 (CC BY - NC 3.0)
<http : //creativecommons.org/licenses/by - nc/3.0/>
Items made from the pattern may be sold;
the pattern may not be sold.

End of Licensing paragraph.
'''

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *

class Design(designBase):

    def pattern(self) :
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        # The designer must supply certain information to allow
        #   tracking and searching of patterns
        #
        # This group is all mandatory
        #
        self.setInfo('patternNumber', 'MR_B1')
        self.setInfo('patternTitle', 'Spencer Bodice Short')
        self.setInfo('companyName', 'Next Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Women's bodice block pattern with minimum ease, includes long sleeve with elbow dart.""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'Block')
        #
        # The next group are all optional
        #
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        self.setInfo('yearstart', '1900')
        self.setInfo('yearend', '')
        self.setInfo('culture', 'European')
        self.setInfo('wearer', '')
        self.setInfo('source', '')
        self.setInfo('characterName', '')
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')

        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'bodice'
        bodice = self.addPattern('bodice')

        #create pattern pieces,  assign an id lettercd 
        A = bodice.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Bodice Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        # points are always in the 'reference' group, and always have style='point_style'

        #---Front A---#
        #f_bust_ease = 0.083 * CD.bust/4.0 #3" for 36" bust
        #f_bust_ease = 0.07 * CD.bust/4.0 #2.5" for 36" bust
        f_bust_ease = 0.035 * CD.bust/4.0 #1.25" for 36" bust
        b_bust_ease = f_bust_ease
        #f_waist_ease = 0.0625 * CD.waist/4.0 #1.5" for 24" waist
        f_waist_ease = 0.03125 * CD.waist/4.0 #.75" for 24" waist
        b_waist_ease = f_waist_ease
        
        f_underarm_height = 9.0 * CM
        f_bust_height = 18 * CM
        b_underarm_height = 18.0 * CM
        f_undearm_height = 9.0 * CM
            
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', left(FSH, 0.5 * CD.front_shoulder_width)) #front shoulder width
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FSW.x))) #front shoulder point
        FNS = A.addPoint('FNS', rightmostP(onCircleAtY(FSP, CD.shoulder, FSH.y))) #front neck side
        FUC = A.addPoint('FUC', down(FNC, f_underarm_height)) #front underarm center
        FBC = A.addPoint('FBC', down(FNC, f_bust_height)) #bust center
        FBP = A.addPoint('FBP', left(FBC, 0.5 * CD.bust_distance)) #bust point
        #FAS = A.addPoint('FAS', left(FUC, CD.across_chest / 2.0 + f_bust_ease / 2.0 )) #temp front armscye point
        #FAS = A.addPoint('FAS', left(FUC, CD.across_chest / 2.0)) #temp front armscye point
        f10 = A.addPoint('f10', left(FUC, CD.across_chest / 2.0)) #temp front armscye point
        FAC = A.addPoint('FAC', midPoint(FNC, FUC))  
        FAS = A.addPoint('FAS', left(FAC, 0.95 * CD.across_chest / 2.0)) #front armscye point 
        f1 = A.addPoint('f1', left(FUC, CD.front_underarm / 2.0)) #temp front underarm side               
        f2 = A.addPoint('f2', leftmostP(tangentPointOnCircle(FBP, (CD.front_bust - CD.bust_distance) / 2.0, f1))) #temp front bust side
        f3 = A.addPoint('f3', onLineAtLength(f1, f2, CD.side)) #temp front waist side
        f4 = A.addPoint('f4', (FBP.x, FWC.y)) #temp dart inside leg
        f5 = A.addPoint('f5', lowestP(intersectCircles(FBP, distance(FBP, f4), f3, CD.front_waist/2.0 - distance(FWC, f4)))) #temp dart outside leg
        
        f6 = A.addPoint('f6', polar(f3, f_waist_ease, angleOfLine(FBP, f2))) #temp front waist side, incl. ease
        f7 = A.addPoint('f7', polar(f1, f_bust_ease, angleOfLine(FBP, f2))) #temp front underarm side, incl. ease                                              
        FBS = A.addPoint('FBS', intersectLines(f7, f6, FBP, f2)) #front bust side, incl. ease 
        FUS = A.addPoint('FUS', onLineAtLength(f7, FBS, 0.15 * CD.side)) #front underarm side        
        #rotate waist point
        total_dart_angle = angleOfVector(f5, FBP, f4)        
        FWS = A.addPoint('FWS', rotate(FBP, f6, -total_dart_angle / 2.0)) #front waist side
        #create bust side dart
        FD2 = A.addPoint('FD2', FBP) #set to be FBP temporarily
        FD2.i = A.addPoint('FD2.i', onLineAtY(f6, f7, FBP.y)) #bust side dart inside leg - fold up toward FUS
        FD2.o = A.addPoint('FD2.o', rotate(FBP, FD2.i, -total_dart_angle / 2.0)) #bust side dart outside leg
        updatePoint(FD2, polar(FBP, 0.12 * distance(FBP, FD2.o), angleOfLine(FD2, FD2.i) - angleOfVector(FD2.o, FBP, FD2.i) / 2.0)) #move FD2
        #reduce & rotate bust waist point
        FD1 = A.addPoint('FD1', down(FBP, 0.12 * abs(FBP.y - FWC.y))) #front dart point        
        FD1.o = A.addPoint('FD1.o', intersectLineRay(FWC, f4, FBP, ANGLE90 + total_dart_angle / 4.0)) #bust waist dart outside leg 
        FD1.i = A.addPoint('FD1.i', intersectLineRay(FWC, f4, FBP, ANGLE90 - total_dart_angle / 4.0)) #bust waist dart inside leg - fold in toward FWC
 

        #extend leg lengths to smooth seamline at dart, then extend middle length so foldline meets seamline
        extendDart(FWC, FD1, FWS)
        foldDart(FD1, FWC) #creates FD1.m for seamline, FD1.ic & FD1.oc for dartline
        extendDart(FUS, FD2, FWS)
        foldDart(FD2, FUS) #creates FD2.m for seamline, FD2.ic & FD2.oc for dartline    
       
        #front control points
        #b/w FNS & FNC
        FNS.addOutpoint(polar(FNS, 0.5 * abs(FNC.y - FNS.y), angleOfLine(FSP, FNS) + ANGLE90))        
        FNC.addInpoint(left(FNC, 0.6 * abs(FNC.x - FNS.x)))
        #b/w FWC & FD1.i
        FWC.addOutpoint(left(FWC, 0.33 * distance(FWC, FD1.i)))
        FD1.i.addInpoint(intersectLineRay(FWC, f4, FD1.i, angleOfLine(FD1, FD1.i) + ANGLE90))
        #b/w FD1.o & FWS
        FD1.o.addOutpoint(intersectLineRay(FWS, f4, FD1.o, angleOfLine(FD1, FD1.o) + ANGLE90))
        FWS.addInpoint(polar(FWS, 0.33 * distance(FD1.o, FWS), angleOfLine(FWS, FUS) + ANGLE90))        
        #b/w FUS & FAS
        FUS.addOutpoint(polar(FUS, 0.4 * distance(FUS, FAS), angleOfLine(FBS, FBP)))
        FAS.addInpoint(down(FAS, 0.5 * distance(FUS, FAS)))
        #b/w FAS & FSP
        FAS.addOutpoint(up(FAS, 0.33 * distance(FAS, FSP)))
        FSP.addInpoint(polar(FSP, 0.15 * distance(FAS, FSP), angleOfLine(FSP, FNS) + ANGLE90))
                          
        #---Back B---#

        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', right(BSH, 0.5 * CD.back_shoulder_width)) #back shoulder width
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BSW.x))) #back shoulder point
        BUC = B.addPoint('BUC', down(BNC, b_underarm_height)) #back underarm center 
        b7 = B.addPoint('b7', right(BUC, CD.across_back / 2.0 + b_bust_ease / 2.0))
        BAC = B.addPoint('BAC', up(BUC, distance(BUC, BNC) / 3.0)) #back armscye center        
        BAS = B.addPoint('BAS', up(b7, distance(b7, BSP) / 3.0)) #back armscye point                    
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BSP, CD.shoulder, BSH.y))) #back neck side
        b1 = B.addPoint('b1', right(BUC, CD.back_underarm / 2.0)) #temp back underarm side               
        #back waist dart        
        BD1 = B.addPoint('BD1', onLineAtY(BWC, BSP, BUC.y)) #back waist dart point
        b2 = B.addPoint('b2', (BD1.x, BWC.y)) #temp dart midPoint at waist
        BD1.i = B.addPoint('BD1.i', left(b2, 0.2 * abs(BD1.x - BWC.x))) #back waist dart inside leg
        BD1.o = B.addPoint('BD1.o', right(b2, 0.2 * abs(BD1.x - BWC.x))) #back waist dart outside leg
        #back waist side & bust side
        b5 = B.addPoint('b5', lowestP(intersectCircles(b1, CD.side, BD1.o, CD.back_waist / 2.0 - distance(BWC, BD1.i)))) #temp back waist side
        b6 = B.addPoint('b6', right(b1, b_bust_ease)) #temp back underarm side
        BWS = B.addPoint('BWS', right(b5, b_waist_ease)) #temp back waist side
        BUS = B.addPoint('BUS', onLineAtLength(b6, BWS, 0.15 * CD.side))
        #smooth dart at waist
        extendDart(BWC, BD1, BWS)
        foldDart(BD1, BWC)
        
        #back shoulder dart
        shoulder_dart_width = 0.07 * CD.shoulder
        BD2 = B.addPoint('BD2', intersectLineRay(BNS, BAS, midPoint(BNS, BSP), angleOfLine(BNS, BSP) + ANGLE90)) #back shoulder dart point        
        BD2.o = B.addPoint('BD2.o', midPoint(BNS, BSP)) #back shoulder dart outside leg
        shoulder_dart_angle = angleOfChord(shoulder_dart_width, distance(BD2, BD2.o))         
        BD2.i = B.addPoint('BD2.i', rotate(BD2, BD2.o, -shoulder_dart_angle)) #back shoulder dart inside leg
        updatePoint(BNS, rotate(BD2, BNS, -shoulder_dart_angle))
        foldDart(BD2, BNS) #fold dart toward BNS
        
        #back control points
        #b/w BNS & BNC
        BNC.addInpoint(right(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, 0.5 * abs(BNC.y - BNS.y), angleOfLine(BNS, BNC.inpoint)))
        #b/w BWC & BD1.i
        BWC.addOutpoint(right(BWC, 0.33 * distance(BWC, BD1.i)))
        BD1.i.addInpoint(intersectLineRay(BWC, b2, BD1.i, angleOfLine(BD1.i, BD1) + ANGLE90))
        #b/w BD1.o & BWS
        BD1.o.addOutpoint(intersectLineRay(BWS, b2, BD1.o, angleOfLine(BD1, BD1.o) + ANGLE90))
        BWS.addInpoint(polar(BWS, 0.33 * distance(BD1.o, BWS), angleOfLine(BWS, BD1.o.outpoint)))                 
        #b/w BUS & BAS
        BUS.addOutpoint(polar(BUS, 0.33 * abs(BUS.x - BAS.x), angleOfLine(BWS, BUS) - ANGLE90))
        BAS.addInpoint(b7)
        #b/w BAS & BSP
        BAS.addOutpoint(up(BAS, 0.33 * distance(BAS, BSP)))
        BSP.addInpoint(polar(BSP, 0.15 * distance(BAS, BSP), angleOfLine(BSP, BNS) - ANGLE90))
        
        #---Sleeve C---#
        #get front & back armcye length
        bl_armscye_length = curveLength(points2List(BUS, BUS.outpoint, BAS.inpoint, BAS)) #back lower armscye length
        bu_armscye_length = curveLength(points2List(BAS, BAS.outpoint, BSP.inpoint, BSP)) #back upper armscye length
        b_armscye_length = bl_armscye_length + bu_armscye_length #back armscye length        
        fl_armscye_length = curveLength(points2List(FUS, FUS.outpoint, FAS.inpoint, FAS)) #front lower armscye length
        fu_armscye_length = curveLength(points2List(FAS, FAS.outpoint, FSP.inpoint, FSP)) #front upper armscye length
        f_armscye_length = fl_armscye_length + fu_armscye_length # front armscye length                        
        armscye_length = f_armscye_length + b_armscye_length #total armscye length
  
        #based loosely on Hillhouse & Mansfield
        SCM = C.addPoint('SCM', (0,0)) #sleeve cap middle - top of sleeve
        SUM1 = C.addPoint('SUM1', down(SCM, CD.oversleeve_length - CD.undersleeve_length)) #temp sleeve underarm middle 
        SUM = C.addPoint('SUM', down(SCM, 1.15 * distance(SCM, SUM1))) #sleeve underarm midPoint                       
        SWM = C.addPoint('SWM', down(SUM, CD.undersleeve_length)) #sleeve wrist middle               
        SUFm = C.addPoint('SUFm', right(SUM, (1.10 * CD.bicep) / 4.0)) #temp 1 front underarm point
        SUBm = C.addPoint('SUBm', left(SUM, (1.10 * CD.bicep) / 4.0)) #temp 1 front underarm point         
        SEM = C.addPoint('SEM', midPoint(SUM, SWM)) #sleeve elbow middle
        SEF1 = C.addPoint('SEF1', right(SEM, (1.10 * CD.elbow) / 4.0)) #temp sleeve elbow front        
        SEB1 = C.addPoint('SEB1', left(SEM, (1.10 * CD.elbow) / 4.0)) #temp sleeve elbow back 
        SCF = C.addPoint('SCF', onLineAtY(SUFm, SEF1, SCM.y)) #sleeve cap front
        SCB = C.addPoint('SCB', onLineAtY(SUBm, SEB1, SCM.y)) #sleeve cap back
        SWF1 = C.addPoint('SWF1', onLineAtY(SUFm, SEF1, SWM.y)) #temp sleeve wrist front
        s1 = C.addPoint('s1', midPoint(SUFm, SCF))
        s2 = C.addPoint('s2', onLineAtLength(s1, SCF, 0.75*IN))
        s3 = C.addPoint('s3', midPoint(SUBm, SCB))
        s4 = C.addPoint('s4', onLineAtLength(s3, SCB, 0.75*IN))
        s5 = C.addPoint('s5', left(SCF, distance(SCF, SCM) / 4.0))
        s6 = C.addPoint('s6', right(SCB, distance(SCB, SCM) / 3.0))
        s7 = C.addPoint('s7', midPoint(SUM, SUFm))
        s8 = C.addPoint('s8', left(SUM, 1*IN)) 
        s10 = C.addPoint('s10', onLineAtLength(s4, s6, (distance(s4, s6) / 2.0) - (1/8.0)*IN)) 
        s11 = C.addPoint('s11', midPoint(s2, s7))
        s12 = C.addPoint('s12', midPoint(s4, s8))
        SUF = C.addPoint('SUF', reflect(s2, angleOfLine(s2, s1), SUM)) #temp 2 sleeve underarm front
        SUB = C.addPoint('SUB', reflect(s4, angleOfLine(s4, s3), SUM)) #temp 2 sleeve underarm back
        SEF = C.addPoint('SEF', reflect(s2, angleOfLine(s2, s1), SEM)) #sleeve elbow front       
        SEB = C.addPoint('SEB', reflect(s4, angleOfLine(s4, s3), SEM)) #sleeve elbow back
 
        #control points
        SCM.addInpoint(midPoint(s6, SCM))        
        SCM.addOutpoint(midPoint(SCM, s5))
        #front sleeve cap 
        SUF.addInpoint(polar(SUF, distance(SUF, SUFm) / 2.0, angleOfLine(SUF, SUFm)))
        s2.addInpoint(polar(s2, distance(SCM, s2) / 3.0, angleOfLine(s2, s5)))
        s2.addOutpoint(polar(s2, distance(s2, SCF) / 3.0, angleOfLine(s2.inpoint, s2)))               
             
        #back sleeve cap      
        SUB.addOutpoint(polar(SUB, distance(SUB, s4) / 3.0, angleOfLine(SUB, SUBm)))
        s4.addInpoint(polar(s4, distance(SUB, s4) / 3.0, angleOfLine(s6, s4)))
        s4.addOutpoint(midPoint(s10, s6))
     
        #adjust front upper fu sleeve cap           
        fu_sleevecap_length = curveLength(points2List(SCM, SCM.outpoint, s2.inpoint, s2))
        fu_diff = fu_sleevecap_length - fu_armscye_length                                 
        while (abs(fu_diff) > 2.0):
            pnt = onLineAtLength(s2, s2.inpoint, fu_diff) #move s2 towards s2.inpoint if sleevecap is too small           
            updatePoint(s2, pnt)
            fu_sleevecap_length = curveLength(points2List(SCM, SCM.outpoint, s2.inpoint, s2)) 
            fu_diff = fu_sleevecap_length - fu_armscye_length
                                  
        #adjust front lower fl sleeve cap           
        fl_sleevecap_length = curveLength(points2List(s2, s2.outpoint, SUF.inpoint, SUF))
        fl_diff = fl_sleevecap_length - fl_armscye_length                       
        while (abs(fl_diff) > 2.0):
            pnt = onLineAtLength(SUF, SUF.inpoint, fl_diff) #move SUF towards SUF.inpoint if sleevecap is too big            
            updatePoint(SUF, pnt)
            fl_sleevecap_length = curveLength(points2List(s2, s2.outpoint, SUF.inpoint, SUF))           
            fl_diff = fl_sleevecap_length - fl_armscye_length
        
        #adjust back upper bu sleeve cap           
        bu_sleevecap_length = curveLength(points2List(s4, s4.outpoint, SCM.inpoint, SCM))
        bu_diff = bu_sleevecap_length - bu_armscye_length                           
        while (abs(bu_diff) > 2.0):
            pnt = onLineAtLength(s4, s4.outpoint, bu_diff) #move s4 towards s4.outpoint if sleevecap is too big     
            updatePoint(s4, pnt)
            bu_sleevecap_length = curveLength(points2List(s4, s4.outpoint, SCM.inpoint, SCM))
            bu_diff = bu_sleevecap_length - bu_armscye_length                   
        
        #adjust back lower bl sleeve cap           
        bl_sleevecap_length = curveLength(points2List(SUB, SUB.outpoint, s4.inpoint, s4))
        bl_diff = bl_sleevecap_length - bl_armscye_length                             
        while (abs(bl_diff) > 2.0):
            pnt = onLineAtLength(SUB, SUB.outpoint, bl_diff) #move SUB towards SUB.outpoint if sleevecap is too big            
            updatePoint(SUB, pnt)
            bl_sleevecap_length = curveLength(points2List(SUB, SUB.outpoint, s4.inpoint, s4))
            bl_diff = bl_sleevecap_length - bl_armscye_length

        
        #wrist
        wrist_length = 1.3 * CD.wrist
        SWF = C.addPoint('SWF', onLineAtY(SUF, SEF, SWM.y))
        SWB = C.addPoint('SWB', left(SWF, wrist_length)) 
        #elbow dart
        pnt1 = SEB
        pnt2 = onLineAtLength(SEB, SWB, distance(SEF, SEB) / 8.0)
        pnt3 = midPoint(pnt1, pnt2)
        pnt4 = polar(pnt3, distance(SEF, SEB) / 4.0, angleOfLine(pnt2, pnt1) + ANGLE90)
        SD1 = C.addPoint('SD1', pnt4)
        SD1.i = C.addPoint('SD1.i', SEB)
        SD1.o = C.addPoint('SD1.o', pnt2)
        foldDart(SD1, SUB)
       
        s13 =C.addPoint('s13', onLineAtLength(SD1.o, SWB, distance(SEF, SWF)))
        SWF.addOutpoint(SWF1)
        s13.addInpoint(SWM)                 
                       
        #---all points calculated, now draw pattern---#
                                       
        #Sleeve C
        Cg1 = dPnt((s8.x, s8.y))
        Cg2 = dPnt((Cg1.x, SWM.y - 8.0 * CM))
        C.addGrainLine(Cg1, Cg2)
        pnt1 = dPnt(midPoint(SUM, SEM))
        C.setLetter((SCM.x, pnt1.y), scaleby=15.0)
        C.setLabelPosition((SCM.x, pnt1.y + 2.0 * CM))
        C.addGridLine(['M', SEB1, 'L', SCB, 'L', SCF, 'L', SEF1,
                       'M', SCM, 'L', SEM,        
                       'M', s7, 'L', s2, 'L', s5, 
                       'M', s8, 'L', s4, 'L', s6,
                       'M', s4, 'L', SUM1, 'L', s2,                               
                       'M', SUB, 'L', SUBm, 'L', SUFm, 'L', SUF,
                       'M', SEB, 'L', SEB1, 'L', SEF1, 'L', SEF,
                       'M', SUF, 'L', SEF, 'L', SWF,
                       'M', SUB, 'L', SEB, 'L', SWB,                       
                       'M', s4, 'L', SEB1,                                              
                       'M', s2, 'L', SEF1])
        C.addDartLine(['M', SD1.oc, 'L', SD1, 'L', SD1.ic])     
        pth = (['M', SCM, 'C', s2, 'C', SUF, 'L', SEF, 'L', SWF, 'C', s13, 'L', SD1.o, 'L', SD1.m, 'L', SD1.i, 'L', SUB, 'C', s4, 'C', SCM])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)         

        #Bodice Front A
        pnt1 = dPnt((FNC.x - abs(FNC.x - FSP.x)/2.0, FNC.y + abs(FUC.y - FNC.y)/2.0))
        A.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        A.setLetter(pnt2, scaleby = 10.0)
        AG1 = dPnt((FNC.x - abs(FNS.x - FNC.x)/2.0, abs(FUC.y - FNC.y)/2.0))
        AG2 = down(AG1, 0.75 * CD.front_waist_length)
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', FWC, 'L', FSP, 'L', FSW, 'L', FSH, 'L', FNC, 
                       'M', FBC, 'L', FBP, 'L', FBS, 
                       'M', FUC, 'L', f1, 'L', f7, 'L', f6, 'L', f3, 'L', f1, 
                       'M', FWC, 'L', f4, 'L', FBP, 'L', f5, 'L', f3, 
                       'M', FBP, 'L', FD2, 
                       'M', FAC, 'L', FAS])
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc, 
                       'M', FD2.ic, 'L', FD2, 'L', FD2.oc])
        pth = (['M', FNC, 'L', FWC, 'C', FD1.i, 'L', FD1.m, 'L', FD1.o, 'C', FWS, 
                'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'C', FAS, 'C', FSP, 'L', FNS, 'C', FNC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)
        
        #Bodice Back B
        pnt1 = dPnt((BNS.x, BNC.y + abs(BUC.y - BNC.y)/2.0))
        B.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        B.setLetter(pnt2, scaleby = 10.0)
        BG1 = dPnt((BNC.x + abs(BNS.x - BNC.x)/2.0, abs(BUC.y - BNC.y)/3.0))
        BG2 = down(BG1, 0.75 * CD.back_waist_length)
        B.addGrainLine(BG1, BG2)
        B.addGridLine(['M', BWC, 'L', BSP, 'L', BSW, 'L', BSH, 'L', BUC, 'L', b6, 'L', BUS, 
                       'M', b1, 'L', b5, 'L', BWS, 
                       'M', BAC, 'L', BAS])
        B.addDartLine(['M', BD1.oc, 'L', BD1, 'L', BD1.ic, 
                       'M', BD2.oc, 'L', BD2, 'L', BD2.ic])
        pth = (['M', BNC, 'L', BWC, 'C', BD1.i, 'L', BD1.m, 'L', BD1.o, 'C', BWS, 'L', BUS, 'C', BAS, 'C', BSP, 
                'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth) 
        
              

        #call draw() to generate svg file
        self.draw()

        return

