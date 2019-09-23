#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#^###################################################### modules
from numpy       import array
from turtle      import *
from math        import * #            overwrites turtle.degrees
from collections import namedtuple
#@################################################# global stuff
vertex = {}  # yeah!                                          '
edges = []   # wow!                                           '
ctrlseq = [] # control sequence                               '
pathdir = [] # path starting and ending vertices              '
mxcoor = 200 # maximum coordinate values                      '
## .. ##########################################################
def φ(x, y): return degrees(atan2(y, x)) #                  --
##################### ,, #######################################
def β(vA,vB,vC): # get oriented angle ABC                      #
    u = vA.coor - vB.coor #-B-wise-A-coors------------|#
    v = vC.coor - vB.coor #-B-wise-C-coors----------------------|#
    β = φ(*v) - φ(*u) #                                        # 
    if β < 0: β += 360 #                                       #
    return β #_______________________f_________________________#
############################################# o o ##############
class Vertex: # |B|e|p|T|é|k|c|                             ####
    def __init__(self, coor): ##################################
        self.coor = coor ###################__c_oord_inates_####
        self.hood = [] # \n\e\i\g\h\b\o\r\s\\\\\\\\\\\\\\\\\////
    def getdir(self, X): # cross ######################## .o ###
        dir = self.hood[:] # Copy Ninja Kakashi      xo
        dir.remove(X) # cross                               o.
        def ζ(z): return β(vertex[X], self, vertex[z]) # < < < <
        dir = sorted(dir, key = ζ, reverse = True) # ! ¡ ¡ ! ! ¡
        return dir ##############################[ left, right ]        
################## *   *   *   *   *   *   *   *   *   *   * ###
def scale(mx): # scale above mxcoor vtx coors  '   '   '   '  |
    k = mxcoor/mx #                '   '       '   '   '   ' ###
    for v in vertex: vertex[v].coor *= k #     '   '   '   '  |       
##### .. #######################################################
def getline(f): #                                            ##
    while True: #________________&___________________________##
        line = f.readline() #===================================
        if line != '\n': break # |s|k|i|f| |m|p|t|y| |l|i|n|e|z|
    line = line.rstrip('\n') #                               ##
    line = line.split(' ') #####################################
    while '' in line: #       #       #       #       #       #
        line.remove('') #|r|m| |m|t|y| |n|3|e\s|################
    return line ################################################
###===################# '' ############################geraut###
def getinfut(): #___________________g_er___i_____nf__ut______###
    global ctrlseq, pathdir #_______ _  ___ _____  __  ______###
    allcoor = [] #_all_coo__________r_di___n_____at__es______###
    with open(0) as f: #_stdin______ _  ___ _____  __  ______###
        n = int(getline(f)[0]) #____ _  ___ _____  __  ______###
        for j in range(n): #________ _  ___ _____  __  ______###
            line = getline(f) #_____ _  ___ _____  __  ______###
            coor = array(line[1:] , dtype = float) #_  ______###
            allcoor.extend(coor) #__     _      _  __  ______###
            vertex[line[0]] = Vertex(coor) #    _  __  ______  oo
        n = int(getline(f)[0]) #                _  __  ______###
        for j in range(n): #                    _  __  ______###
            line = getline(f) #                 _  __  ______###
            edges.append(line) #                _  __  ______###
            vertex[line[0]].hood.append(line[1]) # __  ______###  ###
            vertex[line[1]].hood.append(line[0]) # __  ______###
        ctrlseq = getline(f) #                  _  __  ______###
        pathdir = getline(f) #                  _  __  ______###
    allcoor = sorted(allcoor) #                 _  __  ______###
    mx = max(abs(allcoor[0]), allcoor[-1]) #    _  __  ______###
    if mx > mxcoor: scale(mx) #                 _  __  ______###
#+############################################################7#
def canvas(): # setup turtle screen                           |
    screen = Screen() #                                       |
    screen.bgcolor((.1, .1, .9)) # (R, G, B)                  |
    margin = 50 #                                             |
    wid = h8 = 2*(mxcoor + margin) # width and height         |
    ORIG = (-100, 100) # starting position                    |
    setup(wid, h8, *ORIG) ###################################6|#
####=########################################################'7#
def coorsys(): # draw coordinate system                      '
    penup() # pull the pen up                                '
    speed(3) #                                               '
    setpos(-mxcoor, -mxcoor) # lower left corner             '
    pensize(10) #                                            '
    color("red", "darkorange") # pen and fill color          '
    begin_fill() # @ @ @ @ _ @ @ @ @ @ @ @ 2 @ @ @ @ @ @ @ @ ' @
    down() # pull the pen down                               '
    setpos( mxcoor, -mxcoor) # draw a box ```````````````````'``
    setpos( mxcoor,  mxcoor) #                               '
    setpos(-mxcoor,  mxcoor) ############################1###'##
    setpos(-mxcoor, -mxcoor) #                           |   '
    end_fill() ##########################################|###3##
    up() # penup                                         |
    pensize(1) # . . . . . . . . . . . . . . . . . . . . | . . .
    color("#d0cccc") # light gray                        |
    setpos(0, mxcoor) # start drawing center cross       |
    down() #                                             |
    setpos(0, -mxcoor) #                                 |
    up() ####################################2###########|######
    setpos(-mxcoor, 0) ######################'###########3######
    down() # > > > > > > > > > > > > > > > > ' > > > > > > > > >
    setpos(mxcoor, 0) #                      '
    up() #                                   '
    home() # ORIG                            '                 
    color("#eeeeee") # e-e-e                 '
    dot(5) ##################################'#######1#coorsys## 
###Init######################################2#######^######>>##
def init(): # init stuff                             ^
    getinfut() #                                     ^
    ht() # ..      ..   **   xx     ..       **  ,,  ^ ..     ..
    canvas() #                                       ^
    coorsys() #######################################6##### boom
### .. #########################################################
def drawgraph(): # yeah ########################################
    color("#3C200D") ###########################################
    pensize(1.6)  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  
    speed(1) ###################################################
    for e in edges: # draw ############################# edges #
        up() ###################################################
        setpos(*vertex[e[0]].coor) #                   #########   
        down() #####################    **             #########
        setpos(*vertex[e[1]].coor) #          ..       #########
    up() ########################### oo                #########
    speed(3) #######################      8            #########
    for v in vertex: # draw #########################   vertices 
        setpos(*vertex[v].coor) ####################   #########
        color("brown") ##############################  #########
        dot(8) #####################################   #########
        color("black") ##############################       
        write(v, align = 'right', ############################## 
              font = ('MathJax_Fraktur', 18, 'bold')) ##########
################################################## xo ##########
def getwalk(): ############ get vertices from a control sequence 
    x = list(ctrlseq[0]) ########## get control sequence as list
    for i in range(len(x) - 2): ########################### loof
        dir = vertex[x[i + 1]].getdir(x[i]) ### get L-R vertices
        x[i + 2] = dir[x[i + 2] is 'R'] ##### overwrite x[i + 2]
    return x ####?##############################################
############################################################ oo 
def drawalk(walk, colour, size): #_oo___________________________
    print(walk) #_____________oo________________________________
    up() #______________________________________oo______________
    color(colour) #__oo_________________________________________
    pensize(size) #__________________________________oo_________
    setpos(*vertex[walk[0]].coor) #_oo__________________________
    down() #_oo_________________________________________________
    for v in walk[1:]: #_______________oo_______________________
        setpos(*vertex[v].coor) #________________________oo_____
#################################################__y_e_a_h_!__##
Node = namedtuple('Node', ['INFO', 'parent']) #&&  ^^         ##
#################################################        --   ##
def touch(): # getz minimum path from A to B ####    ..       ##
    A, B = pathdir[0] ###########################      **     ##
    hstk = [A] # history stack ##################  xo         ##
    pstk = [Node(A, None)] # parent stack #######        ^^   ##
    cstk = [] # children stack ##################    00       ##
    while True: #################################     .o      ##
        for p in pstk: # parent loop ############         ,,  ##
            vex = vertex[p.INFO] # BepTèkc ######   oo        ##
            for c in vex.hood: # children loop ##        xx   ##
                if c in hstk: continue # skip ###    **       ##
                node = Node(c, p) ########## boom            OO        #
                if c is B: return node # vearedon    ^^       ##      
                cstk.append(Node(c, p)) #### push       ``    ##
                hstk.append(c) ########### record  ..         ##
        pstk, cstk = cstk, [] # svitch ##########         ::  ##
################################################################
def getpath(): # get minimum path as list of vertex IDs >>>>>>>>
    node = touch() #__*___:___`___-___~___!___?___)___+___&___%_
    path = [] #"___.___,_______*___:___`___-___~___!___?___)___+
    while node: #_.___,_______*___:___`___-___~___!___?___)___+_
        path.append(node.INFO) #_~___!___?___)___+___&___%___@__
        node = node.parent #:___`___-___~___!___?___)___+___&___
    path.reverse() #_.___,_______*___:___`___-___~___!___?___)__
    return path #_^___"___.___,_______*___:___`___-___~___!___?_
def getctrl(path): #############################################
    ctrl = path[:2] #      #      #      #      #      #      #
    getctrl.dir = ('L', 'R') ###################################
    for j in range(1, len(path) - 1): #      #      #      #    
        dir = vertex[path[j]].getdir(path[j - 1]) ##############
        ctrl.append(getctrl.dir[(path[j + 1] == dir[1])]) #
    return(ctrl) ###############################################
def špam(): ###################################### main function
    init() #                                                   #
    drawgraph() #                                              #
    drawalk(getwalk(), "pink", 2) #                            #
    path = getpath() #                                         #
    drawalk(path, "blue", 3) #                                 #
    print(getctrl(path)) #                                     #
    exitonclick() #                                            #
špam() #################################################### log:
