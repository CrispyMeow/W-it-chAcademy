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

    if keys[pygame.K_a] and X > vel:
        if X < 43 or (148-15 < X < 943 and Y < 88) or (133 + 15 + 15 > X and Y < 103 + 15) or ( 73 + 30 > X and Y < 148) or (478 < X < 598 + 15 and 103 < Y < 178) or (388 < X < 478 + 15 and 103 < Y < 178)\
            or (298 < X < 388 + 15 and 103 < Y < 178) or (973 < X < 1048 + 15 and 193 < Y < 253) or (73 < X < 1048 + 15 and 193 < Y < 238) or (73 < X < 118 + 15 and 193 < Y < 253)\
                or (508 < X < 898 + 15 and ((253 < Y < 283) or (283 < Y < 313) or (313 < Y < 343) or (343 < Y < 373) or (373 < Y < 403) or (403 < Y < 448) or (448 < Y < 508)))\
                    or (148 < X < 343 + 15 and ((253 < Y < 283) or (283 < Y < 313) or (313 < Y < 343) or (343 < Y < 373) or (373 < Y < 403) or (403 < Y < 448) or (448 < Y < 508))):
            X -= 0
        else:
            X -= vel
        RIGHT = False
        LEFT = True
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        if X > 1153-15 or (148-15 < X < 943 and Y < 88) or (Y < 103+15 and X > 913-15) or (Y < 133+15 and X > 1033-15) or (478 - 15 < X < 598 and 103 < Y < 178) or (388 - 15 < X < 478 and 103 < Y < 178)\
            or (298 - 15 < X < 388 and 103 < Y < 178) or (X > 1138 - 15 and 193 < Y < 253) or (973 - 15 < X < 1048 and 193 < Y < 253) or (73 - 15 < X < 1048 and 193 < Y < 238)\
                or (73 - 15 < X < 118 and 193 < Y < 253) or (508 - 15 < X < 898 and ((253 < Y < 283) or (283 < Y < 313) or (313 < Y < 343) or (343 < Y < 373) or (373 < Y < 403)\
                    or (403 < Y < 448) or (448 < Y < 508))) or (148 - 15 < X < 343 and ((253 < Y < 283) or (283 < Y < 313) or (313 < Y < 343) or (343 < Y < 373) or (373 < Y < 403) \
                        or (403 < Y < 448) or (448 < Y < 508))):
            X += 0
        else:
            X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        if (478 < X < 598 and 103 - 15 < Y < 178) or (388 < X < 478 and 103 - 15 < Y < 178) or (298 < X < 388 and 103 - 15 < Y < 178) or (X > 1138 and 193 - 15 < Y < 253) or (973 < X < 1048 and 193 - 15< Y < 253)\
            or (73 < X < 1048 and 193 - 15 < Y < 238) or (73 < X < 118 and 193 - 15 < Y < 253) or (Y > 568 - 15) or (508 < X < 898 and ((253 - 15 < Y < 283) or (283 - 15 < Y < 313) or (313 -15 < Y < 343)\
                or (343 - 15 < Y < 373) or (373 - 15 < Y < 403) or (403 - 15 < Y < 448) or (448 - 15 < Y < 508))) or (148 < X < 343 and ((253 - 15 < Y < 283) or (283 - 15 < Y < 313) or (313 - 15 < Y < 343) or (343 - 15 < Y < 373) \
                    or (373 - 15 < Y < 403) or (403 - 15 < Y < 448) or (448 -15 < Y < 508))):
            Y += 0
        else:
            Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        if (Y < 88+15) or (Y < 103+30 and X > 913) or (Y < 133+30 and X > 1033) or (133 + 15 > X and Y < 103 + 30) or ( 73 + 15 > X and Y < 148 + 15) or (478 < X < 598 and 103 < Y < 178 + 15)\
            or (388 < X < 478 and 103 < Y < 178 + 15) or (298 < X < 388 and 103 < Y < 178 + 15) or (X > 1138 and 193 < Y < 253 + 15) or (973 < X < 1048 and 193 < Y < 253 + 15)\
                or (73 < X < 1048 and 193 < Y < 238 + 15) or (73 < X < 118 and 193 < Y < 253 + 15) or (508 < X < 898 and ((253 < Y < 283 + 15) or (283 < Y < 313 + 15) or (313 < Y < 343 + 15)
                    or (343 < Y < 373 + 15) or (373 < Y < 403 + 15) or (403 < Y < 448 + 15) or (448 < Y < 508 + 15))) or (148 < X < 343 and ((253 < Y < 283 + 15) or (283 < Y < 313 + 15) or (313 < Y < 343 + 15)
                    or (343 < Y < 373 + 15) or (373 < Y < 403 + 15) or (403 < Y < 448 + 15) or (448 < Y < 508 + 15))):
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

    if keys[pygame.K_a] and X > vel:
        if (X < 28 + 15) or (((268 < X < 328 + 15) or (568 < X < 628 + 15)) and Y < 418) or (((418 - 15 < X < 418 + 15) or (118 - 15 < X < 118 + 15)) and 343 < Y < 418) \
            or (((58-15 < X < 88) or (118-15 < X < 148) or (178-15 < X < 208) or (238-15 < X < 268)) and (178-15 < Y < 298)) \
            or (((358-15 < X < 388) or (418-15 < X < 448) or (478-15 < X < 508) or (538-15 < X < 568)) and (178-15 < Y < 298)) \
            or ((658-30 < X < 643+30) and (Y < 373)) or (643-30 < X < 673+15) and (Y < 358-15) or ((718-30 < X < 718+15) and (Y < 253)) \
            or (((X < 118+15) or (118+15 < X < 238+15) or (448+15 < X < 568+15) or (568+15 < X < 688+15) or (688+15 < X < 898+15)) and (538-15 < Y < 583+15)) \
            or (((X < 103+15) or (148 < X < 223+15) or (478 < X < 553+15) or (598 < X < 673+15) or (748 < X < 883+15)) and (478 < Y < 523+15)):
            X -= 0
        else:
            X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        if (((268 - 15 < X < 328) or (568 - 15 < X < 628)) and Y < 418) or (((478 - 15 < X < 568 + 15) or (178 - 15 < X < 268 + 15)) and 343 < Y < 418)\
            or ((1153-15 < X) and ((Y < 418) or (Y > 508))) or ((X > 733-15) and (Y < 223+15)) or ((X > 298-15) and (Y > 598-15)) \
            or (((28-15 < X < 73) or (88-15 < X < 118) or (148-15 < X < 193) or (208-15 < X < 268-15)) and (178-15 < Y < 298)) \
            or (((328-15 < X < 373) or (388-15 < X < 418) or (448-15 < X < 493) or (508-15 < X < 568-15)) and (178-15 < Y < 298)) \
            or (((118-15 < X < 118+45) or (448-15 < X < 448+45) or (568-15 < X < 568+45) or (688-15 < X < 688+45)) and (538-15 < Y < 583+15)) \
            or (((28-15 < X < 28+30) or (148-15 < X < 148+30) or (478-15 < X < 478+30) or (598-15 < X < 598+30) or (733-15 < X < 733+30)) and (478 < Y < 523+15)):
            X += 0
        else:
            X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        if (((478 < X < 568 + 15) or (313 < X < 403 + 15) or (193 - 15 < X < 268 + 15) or (28 - 15 < X < 103 + 15)) and 343 - 15 < Y < 418) \
            or (((X < 233) or (X > 313-15)) and (583-15 < Y)) or ((X > 1183-30) and(Y > 523-15)) \
            or ((( X < 103+15) or (118 < X < 223+15) or (448 < X < 553+15) or (568 < X < 673+15) or (688 < X < 868+15)) and (Y > 523-15)) \
            or (((43-15 < X < 88+15) or (163-15 < X < 208+15) or (493-15 < X < 538+15) or (613-15 < X < 658+15) or (763-15 < X < 868+15)) and (Y > 478-15)):
            Y -= 0
        else:
            Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        if (Y < 178 + 15) or (((268 < X < 328) or (568 < X < 628)) and Y < 418 + 15) or (((28 - 15 < X < 103 + 15) or (193 - 15 < X < 403 + 15) or (493 - 15 < X < 598))and 418 - 15 < Y < 418 + 15) \
            or ((X > 1183-30) and Y < 433) or (((778-45 < X) or (598 < X < 718)) and (Y < 238+15)) \
            or (((43-15 < X < 73) or (103-15 < X < 133) or (163-15 < X < 193) or (223-15 < X < 253)) and (238 < Y < 313)) \
            or (((343-15 < X < 373) or (403-15 < X < 433) or (463-15 < X < 493) or (523-15 < X < 553)) and (238 < Y < 313)) \
            or ((628-30 < X < 673-15) and (Y < 373+15)) or ((673-30 < X < 673) and (Y < 373)):
            Y += 0
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

    if keys[pygame.K_a] and X > vel:
        if ((X < 28+15) and ((73-15 < Y < 283+15) or (Y > 433+15))) or ((1108-15 < X < 1108+15) and (103 < Y < 523+15)):
            X -= 0
        else:
            X -= vel
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d]:
        if ((X > 1153-15) and ((73-15 < Y < 238) or (Y > 403)) or ((43-15 < X < 43+15) and (103 < Y < 523+15))):
            X += 0
        else:
            X += vel
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s]:
        if (Y > 583-15) or (58-15 < X < 1093) and (103-15 < Y < 103+30) or ((X > 1168) and (Y > 403-15)):
            Y += 0
        else:
            Y += vel
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w]:
        if (Y < 73+15) or ((58-15 < X < 1093) and (538-15 < Y < 538+30)) or ((X > 1168) and (Y < 253)):
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
def eastcor():
    """eastcorridor map"""
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
def westcor():
    """west corridor map"""
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
def classroom():
    """classroom map"""
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
def eastgar():
    """east garden map"""
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
def eastfor():
    """east forest map"""
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
def forest():
    """forest map"""
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
def research():
    """research room map"""
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
def teachroom():
    """teacher room map"""
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
def apothe():
    """apothecary room map"""
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
def westgar():
    """west garden map"""
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
def westfor():
    """west forest map"""
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
def entry():
    """entry hall map"""
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
def halls():
    """hall (small) map"""
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
    pygame.time.delay(45)
    if gohallway == True: #HALLWAY
        hallway()
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
        elif Y >= 358:
            win.blit(bg ,(rel_x-bg_width, -358))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif gocanteen == True: #CANTEEN
        canteen()
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
        eastcor()
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
        eastcor()
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
        eastgar()
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
        firstaid()
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
        battle()
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
        path()
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
        meeting()
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
        entry()
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
        elif X >= 763 and Y >= 287:
            win.blit(bg ,(-763, -287))
        elif X >= 763:
            win.blit(bg ,(-763, rel_y-bg_height))
        elif Y >= 287:
            win.blit(bg ,(rel_x-bg_width, -287))
        else:
            win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
#------------------------------------
    elif gohalls == True:
        halls()
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
        westgar()
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
        westcor()
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
        westcor()
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
        westfor()
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
        forest()
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
        eastfor()
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
    
    print(X, Y)
    redrawGameWindow()
    pygame.display.update()

pygame.quit()