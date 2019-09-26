#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#^###################################################### modules
from numpy       import array
from turtle      import *
from math        import * #            overwrites turtle.degrees
from collections import namedtuple
#@################################################# global stuff
vertex  = {}  # {id:Vertex}                                    '
edges   = []  # wow!                                           '
ctrlseq = []  # control sequence                               '
ab      = []  # minimum path starting/ending vertices          '
mxcoor  = 200 # maximum coordinate value                       '
##### .. #######################################################
def getline(f): # oo                                          ##
    """ ########################################################
    infut: f - a TextIOWrapper object returned by open
    oufut: list of words
    """ ########################################################
    while True: #_________________&?__________________________##
        line = f.readline() #===================================
        if line != '\n': break # |s|k|i|f| |m|p|t|y| |l|i|n|e|z|
    line = line.rstrip('\n') # discard trailing new line      ##
    line = line.split() #|r|m| |m|t|y| |n|3|e\s| |&| |s|p|l|i|t|
    return line #### xo ########################################
                               
## .. ##########################################################
#|g|e|t| |p|o|l|a|r| |a|n|g|l|e|(|d|e|g|r|e|e|s|)| |i|n| |t|h|e|
#|r|a|n|g|e| |[|-|1|8|0|,| |1|8|0|]| | | | | | | | | | | |e|o|t|
def φ(x, y): return degrees(atan2(y, x)) #                  --
                               #||||||||||||||||||||||||||||||||
##################### ,, ################################# '' ##
#'g'e't' 'o'r'i'e'n't'e'd' 'A'B'C' 'a'n'g'l'e' 'i'n' 't'h'e' ' '
#'r'a'n'g'e' '['0',' '3'6'0')' ' ' ' ' ' ' ' ' ' ' ' ' ' 'e'o't'
def β(A, B, C): #-----------|#
    u = A.coor - B.coor #----------------------------|#
    v = C.coor - B.coor #-------------------------------------|# 
    β = φ(*v) - φ(*u) #-------------------------|#   
    if β < 0: β += 360 #--------------------|# 
    return β #___P___________________f_________________________#

############################################# o_o ##############     
class Vertex: # |B|e|p|T|é|k|c|              (   )          ####
    def __init__(self, coor): ##################################
        self.coor = coor ########################### coordinates
        self.hood = [] # \n\e\i\g\h\b/o\r\s\____________________
        
    ############################################################
    #,g,e,t, ,l,e,f,t, ,a,n,d, ,r,i,g,h,t, ,n,e,i,g,h,b,o,r,s, ,
    #|w|i|t|h| |r|e|s|p|e|c|t| |o|f| |X| | | | | | | | | |e|o|t|
    def getdir(self, X): # cross ######################## .o ###
        '''#####################################################
        infut: X - vtx id
        oufut: list of left and right vtx ids
        '''#####################################################
        dir = self.hood[:] # Copy Ninja Kakashi      xo
        dir.remove(X) # cross                               o.
        def ζ(z): return β(vertex[X], self, vertex[z]) # < < < <
        dir = sorted(dir, key = ζ, reverse = True) # ! ¡ ¡ ! ! ¡
        return dir ##############################[ left, right ]        

################## *   *   *   *   *   *   *   *   *   *   * ###
#|s|c|a|l|e| |v|t|x| |c|o|o|r|z| | | | | | | | | | | | | |e|o|t|
def scale(mx): #   '   '   '   '   '   '   '   '   '   '   '   '
    k = mxcoor/mx #'   '   '   '   '   '   '   '   '   '   '   '
    for v in vertex: vertex[v].coor *= k # '   '   '   '   '   '      

##+===################# '' ############################geraut###
##|r|e|a|d| |i|n|f|u|t| |f|r|o|m| |s|t|d|i|n|,|c|k| |i|f| | |###
##|c|o|o|r|z| |a|r|e| | |i|n| |m|x|c|o|o|r| |r|a|n|g|e|,|i|f|###
##|n|o|t| |s|c|a|l|e| |t|h|e|m|,|f|i|l|l| |g|l|o|b|a|l| | | |###
##|d|a|t|a| | | | | | | | | | | | | | | | | | | | | | |e|o|t|###
def getinfut(): #___________________ ger_infut_______________###
    global ctrlseq, ab #____________    _     _______________###
    ls = [] #_coorz_list____________    _     _______________###
    with open(0) as f: #_stdin______    _     _______________###
        n = int(getline(f)[0]) #____    _     _______________###
        for j in range(n): #________    _     _______________###
            line = getline(f) #_____    _     _______________###
            coor = array(line[1:], dtype = float) #__________###
            ls.extend(coor) #_______    _     _______________###
            vertex[line[0]] = Vertex(coor) #  _______________  oo
        n = int(getline(f)[0]) #____    _     _______________###
        for j in range(n): #________    _     _______________###
            line = getline(f) #_____    _     _______________###
            edges.append(line) #____    _     _______________###
            vertex[line[0]].hood.append(line[1]) # __________###  ###
            vertex[line[1]].hood.append(line[0]) # __________###
        ctrlseq = getline(f) #______    _     _______________###
        ab = getline(f) #___________    _     _______________###
    ls = sorted(ls) #_______________    _     _______________###
    mx = max(abs(ls[0]), ls[-1]) #__    _     _______________###
    if mx > mxcoor: scale(mx) #_____    _     _______________###

#+##############################################################
#|s|e|t|u|p| |t|u|r|t|l|e| |s|c|r|e|e|n| | | | | | | | | |e|o|t|
def canvas(): ##################################################
    screen = Screen() #                                        |
    screen.bgcolor((.1, .1, .9)) # (R, G, B)                   |
    margin = 50 #                                              |
    wid = h8 = 2*(mxcoor + margin) # width and height          |
    ORIG = (-100, 100) # starting position                     |
    setup(wid, h8, *ORIG) ######################################

################################################################
#|d|r|a|w| |c|o|o|r|d|i|n|a|t|e| |s|y|s|t|e|m| | | | | | |e|o|t|
####=########################################################'7#
def coorsys(): #                                             '
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
# |d|r|a|w| |z|e| |g|r|a|p|h| |v|i|t|h| |z|e| |M|a|t|J|a|x| | |
# |f|o|n|t| | | | | | | | | | | | | | | | | | | | | | | |e|o|t|
def drawgraph(): # yeah ########################################
    color("#3C200D") ###########################################
    pensize(1.6)  ##  ##  ##  ##  ##  ##  ##  ##  ##o ##  ##  ##  
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
# |g|e|t| |z|e| |v|t|e|s| |f|r|o|m| |z|e| |c|o|n|t|r|o|l| | | |
# |s|e|q|u|e|n|c|e| |a|z| |a| |l|i|s|t| |o|f| |i|d|s| | | | | |
# | | | | | | | | | | | | | | | | | | | | | | | | | | | |e|o|t|
def getwalk(): ####################################### ge re wok
    x = list(ctrlseq[0]) ########## get control sequence as list
    for i in range(len(x) - 2): ########################### loof
        dir = vertex[x[i + 1]].getdir(x[i]) ### get L-R vertices
        x[i + 2] = dir[x[i + 2] is 'R'] ##### overwrite x[i + 2]
    return x ####??#############################################

############################################################# oo 
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
    A, B = ab[0] ################################      **     ##
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
#################################################  #############

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
