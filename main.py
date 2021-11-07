import pygame

#---------------------------------------------------------------------------
"""set variable"""
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")
bg = pygame.image.load("sprite/meetingroom.jpg")
bg_width, bg_height = bg.get_rect().size
#icon = pygame.image.load("sprite/icongame.png")
#pygame.display.set_icon(icon)
PLAYER_RADIUS = 13
PLAYER_POSITION_X = PLAYER_RADIUS-10
PLAYER_POSITION_Y = 25

start_scrolling_x = (width/2)
stage_wildth = 1280
stage_position_x = 0

start_scrolling_y = height/2
stage_height = 720
stage_position_y = 0

X, Y, vel, WALKCOUNT, CHECK = 448, 238, 15, 0, 'DOWN'

mainClock = pygame.time.Clock()

run = True
LEFT, RIGHT = False, False
DOWN, UP = False, False

gohallway = False
gopath = False
gomeeting = True
gofirstaid = False
gobattle = False
gocanteen = False
goclass_1 = False
goclass_2 = False
goclass_3 = False
gowestgar = False
goeastgar = False
goentry = False
gohalls = False

gowestcor_1 = False
gowestcor_2 = False
goeastcor_1 = False
goeastcor_2 = False

goresearch = False
goteach = False
goapothe = False
gowestfor = False
goeastfor = False
goforest = False

#---------------------------------------------------------------------------
def readvar(file, string):
    """readline variable"""
    f, mylist = open(file, 'r'), []
    while True:
        s = f.readline()
        if s == '':
            break
        d = s.split()
        if d[0].count(string) == 1:
            mylist.append(pygame.image.load(d[0]))
    return mylist

walkr, walkl = readvar('var.txt', 'walkr'), readvar('var.txt', 'walkl')
walkd, walku = readvar('var.txt', 'walkd'), readvar('var.txt', 'walku')
#sup01 = readvar('support.txt', 'sup01')

for i in range(9):
    walkr[i] = pygame.transform.scale(walkr[i], (int(width*0.07), int(height*0.13)))
    walkl[i] = pygame.transform.scale(walkl[i], (int(width*0.07), int(height*0.13)))
    walkd[i] = pygame.transform.scale(walkd[i], (int(width*0.07), int(height*0.13)))
    walku[i] = pygame.transform.scale(walku[i], (int(width*0.07), int(height*0.13)))

#---------------------------------------------------------------------------
def redrawGameWindow():
    """blit the main character"""
    global WALKCOUNT

    if WALKCOUNT + 1 >= 9: #กัน out of range
        WALKCOUNT = 0

    if RIGHT:
        win.blit(walkr[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1

    elif LEFT:
        win.blit(walkl[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1

    elif DOWN:
        win.blit(walkd[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1

    elif UP:
        win.blit(walku[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1
        
    elif RIGHT == False and LEFT == False and DOWN == False and UP == False:
        if CHECK == 'RIGHT':
            win.blit(walkr[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(walkl[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(walkd[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(walku[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
#---------------------------------------------------------------------------
def scrolling():
    """scrolling background"""
    global X
    global Y
    global PLAYER_RADIUS
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    
    #แกนX
    if X > stage_wildth-PLAYER_RADIUS:
        X = stage_wildth-PLAYER_RADIUS
    if X < PLAYER_RADIUS:
        X = PLAYER_RADIUS
    if X < start_scrolling_x:
        PLAYER_POSITION_X = X
    elif X > stage_wildth-start_scrolling_x:
        PLAYER_POSITION_X = X-stage_wildth+width
#     else:
#         PLAYER_POSITION_Y = start_scrolling_y
#         stage_position_y += -vel

    #แกนY
    if Y > stage_height-PLAYER_RADIUS:
        Y = stage_height-PLAYER_RADIUS
    if Y < PLAYER_RADIUS:
        Y = PLAYER_RADIUS
    if Y < start_scrolling_y:
        PLAYER_POSITION_Y = Y
    elif Y > stage_height-start_scrolling_y:
        PLAYER_POSITION_Y = Y-stage_height+height
#     else:
#         PLAYER_POSITION_Y = start_scrolling_y
#         stage_position_y += -vel
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------

SUP_POS_X = 958
SUP_POS_Y = 237
SUPCOUNT = 0
mapping = [pygame.image.load("sprite/hallway.jpg")]

SUP_L = True
SUP_R = False

# def redrawsup():
#     """blit support character"""
#     global bg
#     global SUP_POS_X
#     global SUP_POS_Y
#     global SUPCOUNT
#     global SUP_L
#     global SUP_R

#     if SUP_L:
#         if SUPCOUNT + 1 >= 9:
#             SUPCOUNT = 0
#         SUP_POS_X -= 7.5
#         bg.blit(sup01[SUPCOUNT], (SUP_POS_X, SUP_POS_Y))
#     if SUP_POS_X == 58.0:
#         SUPCOUNT = 9
#         SUP_L = False
#         SUP_R = True
#     if SUP_R:
#         if SUPCOUNT + 1 >= 19:
#             SUPCOUNT = 9
#         SUP_POS_X += 7.5
#         bg.blit(sup01[SUPCOUNT], (SUP_POS_X, SUP_POS_Y))
#     if SUP_POS_X == 965.5:
#         SUP_R = False
#         SUP_L = True
#     SUPCOUNT += 1
#---------------------------------------------------------------------------
def wall(wall=[(0,0,0,0)]):
    """wall"""
    global X
    global Y
    global CHECK
    global RIGHT
    global LEFT
    global DOWN
    global UP
    global PLAYER_RADIUS
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    if keys[pygame.K_a] and X > vel:
        for i,j,k,l in wall:
            print(i,j,k,l)
            print(X, Y)
            if i < X < j and k < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        X -= adam
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        for i,j,k,l in wall:
            print(i,j,k,l)
            print(X,Y)
            if i-15 < X < j-15 and k < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        X += adam
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        for i,j,k,l in wall:
            print(i,j,k,l)
            print(X,Y)
            if i < X < j-15 and k-15 < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        Y += adam
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        for i,j,k,l in wall:
            print(i,j,k,l)
            print(X,Y)
            if i < X < j-15 and k < Y < l:
                adam = 0
                break
            else:
                adam = vel
        Y -= adam
        RIGHT = False
        LEFT = False
        UP = True
        DOWN = False
        CHECK = 'UP'
    else:
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = False

    scrolling()
#---------------------------------------------------------------------------
"""mainloop"""
while run:
    pygame.time.delay(30)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False
#------------------------------------
    if gohallway == True: #HALLWAY
        # redrawsup()
        hall_way = [(0,223,0,103),(283,1280,0,103),(493,553,0,223),(538,1280,0,133),\
            (1168,1280,0,223),(808,1280,133,223),(493,808,133,223),(493,808,253,343),\
            (823,1280,253,343),(1168,1280,253,720),(493,1280,343,720),(493,553,253,720)\
            ,(0,418,133,283),(0,28,0,343),(0,448,388,720),(0,118,0,133),(103,238,0,133),\
            (283,418,0,133),(403,720,0,133),(343,418,253,313),(283,358,253,313),(148,253,253,313),\
            (183,223,253,343),(58,118,253,313),(0,58,253,313)]
        wall(hall_way)
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X == 13 and Y >= 328 and Y <= 388:
            bg = pygame.image.load("sprite/Path.jpg")
            X = 1123
            Y = 343
            gohallway = False
            gopath = True
            gofirstaid = False
            gocanteen = False
        elif Y >= 598:
            bg = pygame.image.load("sprite/entryhall.jpg")
            X = 508
            Y = 47
            gohallway = False
            goentry = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/firstaidroom.jpg")
            Y = 583
            gohallway = False
            gopath = False
            gofirstaid = True
            gocanteen = False
        elif X >= 1198:
            bg = pygame.image.load("sprite/canteen.jpg")
            X = 33
            Y = 163
            gohallway = False
            gopath = False
            gofirstaid = False
            gocanteen = True
        elif X >= 628:
            win.blit(bg ,(-628, rel_y-bg_height))
            bg.blit(mapping[0], (0, 0))
        elif Y >= 358:
            win.blit(bg ,(rel_x-bg_width, -358))
            bg.blit(mapping[0], (0, 0))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            bg.blit(mapping[0], (0, 0))
#------------------------------------
    elif gocanteen == True: #CANTEEN
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X >= 1203:
            X = 28
            Y = 463
            stage_height = 720
            bg = pygame.image.load("sprite/eastcorridor_1.jpg")
            gocanteen = False
            goeastcor_1 = True
        elif Y >= 778 and Y <= 838 and X >= 828:
            X = 28
            Y = 223
            stage_height = 720
            bg = pygame.image.load("sprite/eastgarden.jpg")
            gocanteen = False
            goeastgar = True
        elif X <= 13 and Y >= 148 and Y <= 163:
            X = 1168
            Y = 238
            stage_height = 720
            bg = pygame.image.load("sprite/hallway.jpg")
            gohallway = True
            gocanteen = False
        elif X >= 798 and Y >= 283 and Y <= 523:
            stage_height = 720
            win.blit(bg ,(-453, -283))
        elif X >= 453:
            stage_height = 950
            win.blit(bg ,(-453, rel_y-bg_height))
        else:
            stage_height = 950
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif goeastcor_1 == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X <= 13:
            bg = pygame.image.load("sprite/canteen.jpg")
            X = 1188
            Y = 478
            goeastcor_1 = False
            gocanteen = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/eastcorridor_2.jpg")
            Y = 583
            goeastcor_1 = False
            goeastcor_2 = True
        elif Y >= 628:
            bg = pygame.image.load("sprite/eastgarden.jpg")
            X = 388
            Y = 28
            goeastcor_1 = False
            goeastgar = True
        elif Y >= 178:
            win.blit(bg ,(-28, -178))
        else:
            win.blit(bg ,(-28, rel_y-bg_height))
#------------------------------------
    elif goeastcor_2 == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y >= 632:
            bg = pygame.image.load("sprite/eastcorridor_1.jpg")
            Y = 28
            goeastcor_2 = False
            goeastcor_1 = True
        elif X <= 13:
            bg = pygame.image.load("sprite/battleroom.jpg")
            X = 1198
            Y = 343
            goeastcor_2 = False
            gobattle = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/eastforest.jpg")
            X = 1123
            Y = 613
            goeastcor_2 = False
            goeastfor = True
        else:
            win.blit(bg ,(-28, -13))
#------------------------------------
    elif goeastgar == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X <= 13:
            bg = pygame.image.load("sprite/canteen.jpg")
            stage_height = 950
            X = 813
            Y = 823
            goeastgar = False
            gocanteen = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/eastcorridor_1.jpg")
            X = 433
            Y = 613
            goeastgar = False
            goeastcor_1 = True
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif gofirstaid == True: #FIRSTAID ROOM
        wallfirstaid = [(0,1280,0,178), (0,43,0,720), (0,238,583,720), (298,1280,583,720), (1153,1280,0,418), (1153,1280,523,720), (268,343,0,433), (568,643,0,433), \
        (0,118,343,433), (178,418,343,433,), (478,598,343,433), (28,88,0,298), (88,148,0,298), (148,208,0,298), (208,268,0,298), (328,388,0,298), (388,448,0,298), (448,508,0,298), (508,568,0,298), \
        (0,238,523,720), (463,913,523,720), (28,118,478,553), (148,238,478,553), (478,568,478,553), (598,688,478,553), (748,898,478,553), \
        (613,673,0,388), (643,733,0,253), (643,688,0,358), (733,1280,0,238)]
        wall(wallfirstaid)
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y >= 613:
            bg = pygame.image.load("sprite/hallway.jpg")
            Y = 43
            gohallway = True
            gofirstaid = False
            gobattle = False
        elif X >= 1207:
            bg = pygame.image.load("sprite/battleroom.jpg")
            X = 28
            Y = 373
            gohallway = False
            gofirstaid = False
            gobattle = True
        elif Y >= 13 and X >= 703:
            win.blit(bg ,(-703, -13))
        elif Y >= 13:
            win.blit(bg ,(rel_x-bg_width, -13))
        elif X >= 703:
            win.blit(bg ,(-703, rel_y-bg_height))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif gobattle == True: #BATTLE ROOM
        wallbattle = [(0,43,0,313), (0,43,463,720), (0,1280,0,88), (0,1280,568,720), (1153,1280,0,253), (1153,1280,403,720), (43,1108,103,553)]
        wall(wallbattle)
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X <= 13:
            bg = pygame.image.load("sprite/firstaidroom.jpg")
            X = 1168
            Y = 493
            gobattle = False
            gofirstaid = True
        elif X >= 1222:
            bg = pygame.image.load("sprite/eastcorridor_2.jpg")
            X = 28
            Y = 373
            gobattle = False
            goeastcor_2 = True
        elif X >= 523 and Y >= 103:
            win.blit(bg ,(-523, -103))
        elif Y >= 103:
            win.blit(bg ,(rel_x-bg_width, -103))
        elif X >= 523:
            win.blit(bg ,(-523, -103))
        else:
            win.blit(bg ,(rel_x-bg_width, -103))
#------------------------------------
    elif gopath == True:
        wall_path = [(0, 718, 0, 238), (748, 1280, 0, 238), (118, 658, 222, 297), (808, 1108, 222, 297), (0, 1280, 388, 1280)]
        wall(wall_path)
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X >= 1168:
            bg = pygame.image.load("sprite/hallway.jpg")
            X = 28
            Y = 358
            gohallway = True
            gopath = False
        elif X <= 13:
            bg = pygame.image.load("sprite/westcorridor_1.jpg")
            X = 1183
            Y = 373
            gopath = False
            gowestcor_1 = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/meetingroom.jpg")
            X = 433
            Y = 553
            gopath = False
            gomeeting = True
        elif (X <= 598 and Y >= 313) or (X <= 598 and Y < 313):
            win.blit(bg ,(-598, -313))
        elif X >= 1108:
            win.blit(bg ,(-1108, -313))
        elif Y < 313 or Y >= 313:
            win.blit(bg ,(rel_x-bg_width, -313))
#------------------------------------
    elif gomeeting == True: #MEETING ROOM
        meeting_wall = [(0,1280,0,103),(913,1280,0,133),(1033,1280,0,163),(1153,1280,0,720),(448,1280,568,720),(0,418,568,720),(0,43,0,720),(0,148,0,88),(0,163,0,133),(0,103,0,163),(298,388,103,148),(298,388,133,193)
                        ,(388,478,103,148),(388,493,133,198),(478,598,103,148),(478,613,133,198),(73,1063,193,253),(73,133,193,268),(973,1063,193,268),(1138,1280,193,268),(508,898,253,298),(508,898,283,328),(508,898,313,358)
                        ,(508,898,343,388),(508,898,373,418),(508,898,403,478),(508,898,463,538),(148,358,253,298),(148,358,283,328),(148,358,313,358),(148,358,343,388),(148,358,373,418),(148,358,403,478),(148,358,463,538)]
        wall(meeting_wall)
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X >= 403 and X <= 448 and Y > 553:
            bg = pygame.image.load("sprite/path.jpg")
            gomeeting = False
            gopath = True
            X = 733
            Y = 28
        elif X >= 523 and Y >= 418:
            win.blit(bg ,(-523, -418))
        elif X >= 523:
            win.blit(bg ,(-523, rel_y-bg_height))
        elif Y >= 418:
            win.blit(bg ,(rel_x-bg_width, -418))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif goentry == True:
        wall_entry = [(538,1280,0,92),(1213,1280,0,720),(538,1280,512,720),(0,493,512,720),(478,538,617,720),(0,43,242,720),(0,493,0,92),(583,1183,152,497),(53,433,152,497)\
            ,(538,733,0,122),(928,1280,0,122),(298,493,0,122),(0,178,0,122),(178,298,0,107),(718,898,0,107)]
        wall(wall_entry)
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X <= 13:
            bg = pygame.image.load("sprite/halls.jpg")
            X = 1153
            goentry = False
            gohalls = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/hallway.jpg")
            X = 463
            Y = 583
            goentry = False
            gohallway = True
        elif X >= 763 and Y >= 272:
            win.blit(bg ,(-763, -272))
        elif X >= 763:
            win.blit(bg ,(-763, rel_y-bg_height))
        elif Y >= 272:
            win.blit(bg ,(rel_x-bg_width, -272))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif gohalls == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X <= 13:
            bg = pygame.image.load("sprite/westgarden.jpg")
            X = 1123
            gohalls = False
            gowestgar = True
        elif X >= 1207:
            X = 28
            bg = pygame.image.load("sprite/entryhall.jpg")
            gohalls = False
            goentry = True
        elif X >= 160 and Y >= 287:
            win.blit(bg ,(-160, -287))
        elif X >= 160:
            win.blit(bg ,(-160, rel_y-bg_height))
        elif Y >= 287:
            win.blit(bg ,(rel_x-bg_width, -287))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif gowestgar == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X >= 1207:
            bg = pygame.image.load("sprite/halls.jpg")
            X = 73
            gowestgar = False
            gohalls = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/westcorridor_1.jpg")
            X = 748
            Y = 613
            gowestgar = False
            gowestcor_1 = True
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif gowestcor_1 == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y >= 628:
            bg = pygame.image.load("sprite/westgarden.jpg")
            X = 832
            Y = 28
            gowestcor_1 = False
            gowestgar = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/westcorridor_2.jpg")
            Y = 508
            gowestcor_1 = False
            gowestcor_2 = True
        elif X >= 1198:
            bg = pygame.image.load("sprite/path.jpg")
            X = 28
            Y = 343
            gowestcor_1 = False
            gopath = True
        elif Y >= 365:
            win.blit(bg ,(-28, -365))
        else:
            win.blit(bg ,(-28, rel_y-bg_height))
#------------------------------------
    elif gowestcor_2 == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y >= 613:
            bg = pygame.image.load("sprite/westcorridor_1.jpg")
            Y = 73
            gowestcor_2 = False
            gowestcor_1 = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/westforest.jpg")
            X = 43
            Y = 598
            gowestcor_2 = False
            gowestfor = True
        else:
            win.blit(bg ,(-28, -13))
#------------------------------------
    elif gowestfor == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y >= 628:
            bg = pygame.image.load("sprite/westcorridor_2.jpg")
            gowestfor = False
            gowestcor_2 = True
            X = 598
            Y = 28
        elif X >= 1213:
            bg = pygame.image.load("sprite/forest.jpg")
            X = 28
            gowestfor = False
            goforest = True
        elif X >= 583:
            win.blit(bg ,(-583, -58))
        else:
            win.blit(bg ,(rel_x-bg_width, -58))
#------------------------------------
    elif goforest == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X <= 13:
            bg = pygame.image.load("sprite/westforest.jpg")
            X = 1198
            goforest = False
            gowestfor = True
        elif X >= 1213:
            bg = pygame.image.load("sprite/eastforest.jpg")
            X = 28
            goforest = False
            goeastfor = True
        elif X >= 523 and Y >= 425:
            win.blit(bg ,(-523, -425))
        elif X >= 523:
            win.blit(bg ,(-523, rel_y-bg_height))
        elif Y >= 425:
            win.blit(bg ,(rel_x-bg_width, -425))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif goeastfor == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X <= 13:
            bg = pygame.image.load("sprite/forest.jpg")
            X = 1198
            goeastfor = False
            goforest = True
        elif Y >= 628:
            bg = pygame.image.load("sprite/eastcorridor_2.jpg")
            X = 598
            Y = 28
            goeastfor = False
            goeastcor_2 = True
        elif X >= 583:
            win.blit(bg ,(-583, -58))
        else:
            win.blit(bg ,(rel_x-bg_width, -58))
#---------------------------------------------------------------------------
    
    # print(X, Y)
    redrawGameWindow()
    pygame.display.update()

pygame.quit()
