import pygame

#---------------------------------------------------------------------------
"""set variable"""
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")
bg = pygame.image.load("sprite/secretforest.jpg")
fog = pygame.image.load("sprite/fog.png")
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

X, Y, vel, WALKCOUNT, CHECK = 598, 617, 15, 0, 'UP'
MONCOUNT, MONSTER_POSITION_X, MONSTER_POSITION_Y = 0, 242, 242
hp, fight = 50, False

run = True
LEFT, RIGHT = False, False
DOWN, UP = False, False
gosecretfor = True

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

yellow = [pygame.image.load("sprite/monster/yellow1.png"), pygame.image.load("sprite/monster/yellow2.png"), pygame.image.load("sprite/monster/yellow3.png"),
         pygame.image.load("sprite/monster/yellow4.png"), pygame.image.load("sprite/monster/yellow5.png"), pygame.image.load("sprite/monster/yellow6.png"),
         pygame.image.load("sprite/monster/yellow7.png"), pygame.image.load("sprite/monster/yellow8.png"), pygame.image.load("sprite/monster/yellow9.png")]

damagewalkr = pygame.image.load("sprite/damage taken/walkr1.png")
damagewalkl = pygame.image.load("sprite/damage taken/walkl1.png")
damagewalkd = pygame.image.load("sprite/damage taken/walkd1.png")
damagewalku = pygame.image.load("sprite/damage taken/walku1.png")

for i in range(9):
    walkr[i] = pygame.transform.scale(walkr[i], (int(width*0.07), int(height*0.13)))
    walkl[i] = pygame.transform.scale(walkl[i], (int(width*0.07), int(height*0.13)))
    walkd[i] = pygame.transform.scale(walkd[i], (int(width*0.07), int(height*0.13)))
    walku[i] = pygame.transform.scale(walku[i], (int(width*0.07), int(height*0.13)))
    damagewalkr = pygame.transform.scale(damagewalkr, (int(width*0.07), int(height*0.13)))
    damagewalkl = pygame.transform.scale(damagewalkl, (int(width*0.07), int(height*0.13)))
    damagewalkd = pygame.transform.scale(damagewalkd, (int(width*0.07), int(height*0.13)))
    damagewalku = pygame.transform.scale(damagewalku, (int(width*0.07), int(height*0.13)))
    
#---------------------------------------------------------------------------
def redrawGameWindow():
    """blit the main character"""
    global WALKCOUNT
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    global MONSTER_POSITION_X
    global MONSTER_POSITION_Y

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
            
    if -15 <= MONSTER_POSITION_Y-PLAYER_POSITION_Y <= 60 and \
       abs(MONSTER_POSITION_X-PLAYER_POSITION_X) <= 19:
        if CHECK == 'RIGHT':
            win.blit(damagewalkr, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(damagewalkl, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(damagewalkd, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(damagewalku, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
            
#---------------------------------------------------------------------------
def redrawMonster():
    """blit monster"""
    global MONCOUNT
    global MONSTER_POSITION_X
    global MONSTER_POSITION_Y
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    
    if MONCOUNT + 1 >= 9: #กัน out of range
        MONCOUNT = 0
    if MONSTER_POSITION_X >= PLAYER_POSITION_X+15:
        MONSTER_POSITION_X -= 5
    if MONSTER_POSITION_X <= PLAYER_POSITION_X+15:
        MONSTER_POSITION_X += 5
    if MONSTER_POSITION_Y >= PLAYER_POSITION_Y+25:
        MONSTER_POSITION_Y -= 5
    if MONSTER_POSITION_Y <= PLAYER_POSITION_Y+50:
        MONSTER_POSITION_Y += 5

    win.blit(yellow[MONCOUNT], (MONSTER_POSITION_X, MONSTER_POSITION_Y))
    MONCOUNT += 1
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
def secretfor():
    """secret forest map"""
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
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False
#------------------------------------
    if gosecretfor == True:
        secretfor()
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y <= 257:
            fight = True
        if Y >= 662:
            win.blit(bg ,(-238, -662))
        else:
            win.blit(bg ,(-238, rel_y-bg_height))
#---------------------------------------------------------------------------
    
#     print(X, Y)
#     print('PLAYER', PLAYER_POSITION_X, PLAYER_POSITION_Y)
#     print('MONSTER', MONSTER_POSITION_X, MONSTER_POSITION_Y)

    if fight:
        if MONSTER_POSITION_Y-PLAYER_POSITION_Y <= 26:
            redrawMonster()
            redrawGameWindow()
        else:
            redrawGameWindow()
            redrawMonster()
    else:
        redrawGameWindow()

    if gosecretfor:
        win.blit(fog ,(-238, rel_y-bg_height))
    if -15 <= MONSTER_POSITION_Y-PLAYER_POSITION_Y <= 60 and \
       abs(MONSTER_POSITION_X-PLAYER_POSITION_X) <= 19: #ฝั่งลบ มอนสูงกว่าคน
        hp -= 0.5

    print(hp)
    pygame.display.update()

pygame.quit()
