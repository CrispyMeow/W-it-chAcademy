import pygame

#---------------------------------------------------------------------------
"""set variable"""
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")
bg = pygame.image.load("sprite/hallway.jpg")
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
run = True
LEFT, RIGHT = False, False
DOWN, UP = False, False
gohallway = True
gopath = False
gomeeting = False
gofirstaid = False
gobattle = False
gocanteen = False
goeastcor_1 = False
goeastcor_2 = False
goclass_1 = False
goclass_2 = False
goclass_3 = False
#---------------------------------------------------------------------------

walkr = [pygame.image.load("sprite/walkr1.png"), pygame.image.load("sprite/walkr2.png"), pygame.image.load("sprite/walkr3.png"),
        pygame.image.load("sprite/walkr4.png"), pygame.image.load("sprite/walkr5.png"), pygame.image.load("sprite/walkr6.png"),
        pygame.image.load("sprite/walkr7.png"), pygame.image.load("sprite/walkr8.png"), pygame.image.load("sprite/walkr9.png")]

walkl = [pygame.image.load("sprite/walkl1.png"), pygame.image.load("sprite/walkl2.png"), pygame.image.load("sprite/walkl3.png"),
        pygame.image.load("sprite/walkl4.png"), pygame.image.load("sprite/walkl5.png"), pygame.image.load("sprite/walkl6.png"),
        pygame.image.load("sprite/walkl7.png"), pygame.image.load("sprite/walkl8.png"), pygame.image.load("sprite/walkl9.png")]

walkd = [pygame.image.load("sprite/walkd1.png"), pygame.image.load("sprite/walkd2.png"), pygame.image.load("sprite/walkd3.png"),
        pygame.image.load("sprite/walkd4.png"), pygame.image.load("sprite/walkd5.png"), pygame.image.load("sprite/walkd6.png"),
        pygame.image.load("sprite/walkd7.png"), pygame.image.load("sprite/walkd8.png"), pygame.image.load("sprite/walkd9.png")]

walku = [pygame.image.load("sprite/walku1.png"), pygame.image.load("sprite/walku2.png"), pygame.image.load("sprite/walku3.png"),
        pygame.image.load("sprite/walku4.png"), pygame.image.load("sprite/walku5.png"), pygame.image.load("sprite/walku6.png"),
        pygame.image.load("sprite/walku7.png"), pygame.image.load("sprite/walku8.png"), pygame.image.load("sprite/walku9.png")]

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
def hallway():
    """hallway map"""
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
        if ((X < 238 or X > 283) and Y < 103+15) or (X < 418 and 133 < Y < 282) or (Y < 118 and ( 28 < X < 118-15 or 118 < X < 208 or 312 < X < 418 or 403 < X < 493+15))\
            or (Y < 202 and (493+15 < X < 538+15)) or (Y > 253 and (493+15 < X < 538+15)) or (133 < Y < 295 and ( X < 43+15 or 43+15 < X < 103+15 or 163 < X < 253 or 283+15 < X < 343+15 or 343+15 < X < 418))\
            or ((118+15 < Y < 208 or 238+15 < Y < 328) and (523 < X < 808+15 or 823 < X < 1199+15)) or (178 < X < 223+15 and 298-15 < Y <328) or (Y > 373+15 and X < 433+15) :
            X -= 0
        else:
            X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        if (X > 1183) or ((X > 268 or X < 222) and Y < 103+15) or (Y < 118 and ( 13 < X < 103+15 or 103 < X < 208 or 313-15 < X < 403 or 403-15 < X < 493+15))\
            or (Y < 202 and (493-15 < X < 538)) or (Y > 253 and (493-15 < X < 538)) or (133 < Y < 295 and ( X < 43 or 43 < X < 103 or 133 < X < 238 or 283-15 < X < 343 or 343-15 < X < 403))\
            or ((118+15 < Y < 208 or 238+15 < Y < 328) and (523-15 < X < 808+15 or 823-15 < X < 1183-30)) or (178-15 < X < 223 and 298-15 < Y < 328) \
            or (X > 1183-15 and (Y < 208 or Y > 253)):
            X += 0
        else:
            X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        if (Y > 583) or (118 < Y < 268) and (12 < X < 388+15) or (Y > 253-15 and (493 < X < 538)) or (Y > 373 and X < 433) or (Y > 328 and 523 < X < 1199)\
            or ((118 < Y < 208 or 238 < Y < 328) and (523 < X < 808 or 823 < X < 1199)):
            Y += 0
        else:
            Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        if (Y < 118 and (X < 222-15 or X > 283+15)) or ((133 < Y < 284) and (12 < X < 388+15)) or (Y < 133 and ( 13 <= X < 103 or 118-15 < X < 193+30 or 313-30 < X < 403 or 403 < X < 493+15))\
            or (Y < 217 and (493 < X < 538)) or (133 < Y < 298+15 and ( X < 43 or 43+15 < X < 103 or 148 < X < 238 or 283 < X < 343 or 343 < X < 403))\
            or (Y < 133 and 523 < X < 1199) or ((118+15 < Y < 208+15 or 238+15 < Y < 328+15) and (523 < X < 808 or 823 < X <= 1198)) or (178 < X < 223 and 298-15 < Y < 328+15):
            Y -= 0
        else:
            Y -= vel
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
def path():
    """path map"""
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

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a] and X > vel:
        if (X < 688+30 and Y < 238-15) or ((118 < X < 643+15 or 793 < X < 1093+15) and 237-15 < Y < 297):
            X -= 0
        else:
            X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        if ( X > 763-30 and Y < 238-15) or ((118-15 < X < 643 or 793 < X < 1093) and 237-15 < Y < 297):
            X += 0
        elif X >= 1153 and Y >= 223 and Y <= 298:
            X += 0
        else:
            X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        if Y >= 388:
            Y += 0
        else:
            Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        if (X < 688+15 and Y < 238) or ( X > 763-15 and Y < 238) or ((118 < X < 643 or 793+15 < X < 1093) and 237 < Y < 297+15):
            Y -= 0
        else:
            Y -= vel
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
def meeting():
    """meetingroom map"""
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

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a] and X > vel:
        if X < 43 or (148-15 < X < 943 and Y < 88):
            X -= 0
        else:
            X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        if X > 1153-15 or (148-15 < X < 943 and Y < 88) or (Y < 103+15 and X > 913-15) or (Y < 133+15 and X > 1033-15):
            X += 0
        else:
            X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        if (Y < 88+15) or (Y < 103+30 and X > 913) or (Y < 133+30 and X > 1033):
            Y -= 0
        else:
            Y -= vel
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
def firstaid():
    """firstaidroom map"""
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

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a] and X > vel:
        X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        Y -= vel
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
def battle():
    """battleroom map"""
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

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a] and X > vel:
        X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        Y -= vel
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
def canteen():
    """canteen map"""
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

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a] and X > vel:
        X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        Y -= vel
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
def eastcor_1():
    """eastcorridor_1 map"""
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

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a] and X > vel:
        X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        Y -= vel
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
def eastcor_2():
    """eastcorridor_2 map"""
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

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a] and X > vel:
        X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        Y -= vel
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
def class_1():
    """class_1 map"""
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

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a] and X > vel:
        X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        Y -= vel
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
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False
#------------------------------------
    if gohallway == True: #HALLWAY
        bg = pygame.image.load("sprite/hallway.jpg")
        hallway()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X == 13 and Y >= 328 and Y <= 388:
            X = 1123
            Y -= 15
            gohallway = False
            gopath = True
            gofirstaid = False
            gocanteen = False
        elif Y <= 13:
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
        elif Y >= 358:
            win.blit(bg ,(rel_x-bg_width, -358))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif gocanteen == True: #CANTEEN
        pygame.time.delay(50)
        canteen()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X >= 1203:
            X = 43
            gocanteen = False
            gohallway = False
            goeastcor_1 = True
        if X <= 13 and Y >= 148 and Y <= 163:
            X = 1168
            Y += 75
            gocanteen = False
            gohallway = True
            goeastcor_1 = False
        elif X >= 843 and Y >= 358 and Y <= 508:
            win.blit(bg ,(-483, -358))
        elif X >= 483:
            win.blit(bg ,(-483, rel_y-bg_height))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif goeastcor_1 == True:
        bg = pygame.image.load("sprite/Eastcor_1.jpg")
        eastcor_1()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X <= 13 and Y >= 298 and Y <= 388:
            bg = pygame.image.load("sprite/canteen.jpg")
            X = 1168
            goeastcor_1 = False
            goeastcor_2 = False
            gocanteen = True
        elif Y >= 298 and Y <= 343 and X >= 1222:
            X = 28
            goeastcor_1 = False
            goclass_1 = True
        elif Y >= 28 and Y <= 73 and X >= 1222:
            X = 28
            Y = 328
            goeastcor_1 = False
            goclass_2 = True
        elif Y <= 13 and X <= 883:
            Y = 598
            goeastcor_1 = False
            goeastcor_2 = True
            gocanteen = False   
        elif Y >= 358:
            win.blit(bg ,(-13, -358))
        else:
            win.blit(bg ,(-13, rel_y-bg_height))
#------------------------------------
    elif goeastcor_2 == True:
        bg = pygame.image.load("sprite/Eastcor_2.jpg")
        eastcor_2()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X >= 1222:
            X = 28
            Y = 313
            goeastcor_2 = False
            goclass_3 = True
        elif Y >= 628:
            Y = 28
            goeastcor_2 = False
            goeastcor_1 = True
            gobattle = False
        elif X <= 13:
            X = 1183
            Y = 343
            goeastcor_2 = False
            goeastcor_1 = False
            gobattle = True
        elif Y >= 238:
            win.blit(bg ,(-13, -237))
        else:
            win.blit(bg ,(-13, rel_y-bg_height))
#------------------------------------
    elif goclass_1 or goclass_2 or goclass_3:
        if goclass_1:
            bg = pygame.image.load("sprite/class_1.jpg")
        elif goclass_2:
            bg = pygame.image.load("sprite/class_2.jpg")
        elif goclass_3:
            bg = pygame.image.load("sprite/class_3.jpg")
        class_1()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X <= 13 and (goclass_1 or goclass_2):
            if goclass_2:
                Y = 58
            X = 1198
            goclass_1 = False
            goclass_2 = False
            goclass_3 = False
            goeastcor_1 = True
        if X <= 13 and goclass_3:
            X = 1198
            Y = 208
            goclass_1 = False
            goclass_2 = False
            goclass_3 = False
            goeastcor_2 = True
        elif X >= 508:
            win.blit(bg ,(-508, -148))
        else:
            win.blit(bg ,(rel_x-bg_width, -148))
#------------------------------------
    elif gofirstaid == True: #FIRSTAID ROOM
        bg = pygame.image.load("sprite/firstaidroom.jpg")
        firstaid()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y >= 613:
            Y = 43
            gohallway = True
            gofirstaid = False
            gobattle = False
        elif X >= 1207:
            X = 43
            Y -= 120
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
        bg = pygame.image.load("sprite/battleroom.jpg")
        battle()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X <= 13:
            X = 1168
            Y += 120
            gobattle = False
            gofirstaid = True
            goeastcor_2 = False
        elif X >= 1207:
            X = 28
            Y = 223
            gobattle = False
            gofirstaid = False
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
        bg = pygame.image.load("sprite/Path.jpg")
        path()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        
        if X >= 1168:
            X = 28
            Y += 15
            gohallway = True
            gopath = False
        elif Y <= 13:
            X = 433
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
        bg = pygame.image.load("sprite/meetingroom.jpg")
        meeting()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if X >= 403 and X <= 448 and Y > 553:
            new_width, new_height = 0, -313
            gomeeting = False
            gopath = True
            X += 300
            Y = 43
        elif X >= 523 and Y >= 418:
            win.blit(bg ,(-523, -418))
        elif X >= 523:
            win.blit(bg ,(-523, rel_y-bg_height))
        elif Y >= 418:
            win.blit(bg ,(rel_x-bg_width, -418))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#---------------------------------------------------------------------------

    print(X, Y)
    redrawGameWindow()
    pygame.display.update()

pygame.quit()