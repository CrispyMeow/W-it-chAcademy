import pygame, json

#---------------------------------------------------------------------------
"""set variable"""
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")
bg = pygame.image.load("sprite/entryhall.jpg")
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

X, Y, vel, WALKCOUNT, CHECK = 508, 178, 15, 0, 'DOWN'

mainClock = pygame.time.Clock()

run = True
LEFT, RIGHT = False, False
DOWN, UP = False, False

gohallway = False
gopath = False
gomeeting = False
gofirstaid = False
gobattle = False
gocanteen = False
goclass_1 = False
goclass_2 = False
goclass_3 = False
gowestgar = False
goeastgar = False
goentry = True
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

walls = open("walls.txt", 'r').read()
walls = dict(json.loads(walls))

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
#--------------hallway---------------
    if gohallway == True: #HALLWAY
        # redrawsup()
        wall(walls["hallway"])
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
            Y = 43
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
#--------------canteen---------------
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
#--------------eastcor1--------------
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
#--------------eastcor2--------------
    elif goeastcor_2 == True:
        wall(walls["eastcor2"])
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
#--------------eastgarden------------
    elif goeastgar == True:
        wall(walls["eastgar"])
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
#--------------firstaid--------------
    elif gofirstaid == True: #FIRSTAID ROOM
        wall(walls["firstaid"])
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
#---------------battle---------------
    elif gobattle == True: #BATTLE ROOM
        wall(walls["battle"])
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
#----------------path----------------
    elif gopath == True:
        wall(walls["path"])
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
#--------------meeting---------------
    elif gomeeting == True: #MEETING ROOM
        wall(walls["meeting"])
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
#--------------entryhall-------------
    elif goentry == True:
        wall(walls["entryhall"])
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X <= 13:
            bg = pygame.image.load("sprite/halls.jpg")
            X = 1153
            Y = 178
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
#----------------hall----------------
    elif gohalls == True:
        wall(walls["hall"])
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
#-------------westgarden-------------
    elif gowestgar == True:
        wall(walls["westgar"])
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
#--------------westcor1--------------
    elif gowestcor_1 == True:
        wall(walls["westcor1"])
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
        if 13 <= X <= 28 and 313 <= Y < 388:
            win.fill((255,0,0), rect=[X+20,Y-50,50,50])
            if keys[pygame.K_f]:
                bg = pygame.image.load("sprite/apothecaryroom.jpg")
                X = 973
                Y = 433
                gowestcor_1 = False
                goapothe = True
                CHECK = "LEFT"
        if 13 <= X <= 28 and 103 <= Y < 163:
            win.fill((255,0,0), rect=[X+20,Y-50,50,50])
            if keys[pygame.K_f]:
                bg = pygame.image.load("sprite/teacherroom.jpg")
                X = 958
                Y = 373
                gowestcor_1 = False
                goteach = True
                CHECK = "LEFT"
#--------------westcor2--------------
    elif gowestcor_2 == True:
        wall(walls["westcor2"])
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y >= 613:
            bg = pygame.image.load("sprite/westcorridor_1.jpg")
            Y = 103
            gowestcor_2 = False
            gowestcor_1 = True
        elif Y <= 13:
            bg = pygame.image.load("sprite/westforest.jpg")
            X = 43
            Y = 598
            gowestcor_2 = False
            gowestfor = True
        elif Y >= 73:
            win.blit(bg ,(-28, -73))
        else:
            win.blit(bg ,(-28, rel_y-bg_height))
        if 13 <= X <= 28 and 208 <= Y < 358:
            win.fill((255,0,0), rect=[X+20,Y-50,50,50])
            if keys[pygame.K_f]:
                bg = pygame.image.load("sprite/researchroom.jpg")
                X = 973
                Y = 433
                gowestcor_2 = False
                goresearch = True
                CHECK = "LEFT"
#-------------westforest-------------
    elif gowestfor == True:
        wall(walls["westfor"])
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
            Y = 418
            gowestfor = False
            goforest = True
        elif X >= 583:
            win.blit(bg ,(-583, -58))
        else:
            win.blit(bg ,(rel_x-bg_width, -58))
#--------------forest----------------
    elif goforest == True:
        wall(walls["forest"])
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
#-------------eastforest--------------
    elif goeastfor == True:
        wall(walls["eastforest"])
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
#------------apothecaryroom-----------
    elif goapothe == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X >= 400:
            win.blit(bg ,(-400, -58))
        else:
            win.blit(bg ,(rel_x-bg_width, -58))
        if 1033 <= X <= 1630 and 358 <= Y < 493:
            win.fill((255,0,0), rect=[X+20,Y-50,50,50])
            if keys[pygame.K_f]:
                bg = pygame.image.load("sprite/westcorridor_1.jpg")
                X = 58
                Y = 343
                gowestcor_1 = True
                goapothe = False
                CHECK = "RIGHT"
#------------teacherroom--------------
    elif goteach == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X >= 400:
            win.blit(bg ,(-400, -58))
        else:
            win.blit(bg ,(rel_x-bg_width, -58))
        if 1033 <= X <= 1630 and 358 <= Y < 493:
            win.fill((255,0,0), rect=[X+20,Y-50,50,50])
            if keys[pygame.K_f]:
                bg = pygame.image.load("sprite/westcorridor_1.jpg")
                X = 58
                Y = 133
                gowestcor_1 = True
                goteach = False
                CHECK = "RIGHT"
#------------researchroom-------------
    elif goresearch == True:
        wall()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X >= 400:
            win.blit(bg ,(-400, -58))
        else:
            win.blit(bg ,(rel_x-bg_width, -58))
        if 1033 <= X <= 1630 and 358 <= Y < 493:
            win.fill((255,0,0), rect=[X+20,Y-50,50,50])
            if keys[pygame.K_f]:
                bg = pygame.image.load("sprite/westcorridor_2.jpg")
                X = 58
                Y = 298
                gowestcor_2 = True
                goteach = False
                CHECK = "RIGHT"
#---------------------------------------------------------------------------
    
    # print(X, Y)
    redrawGameWindow()
    pygame.display.update()

pygame.quit()
