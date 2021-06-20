import pygame, math , os ,random
import ball, brick, paddle, position, scoreboard

windowWidth = 1280
windowHeight = windowWidth * 9 // 16
SFX = 0.2
BGM = 0.1
full = False
p_bonus = 1
bonus_time = 5000

def gameloop(screen,lev,lif,sco):
    global windowWidth, windowHeight, SFX, BGM, full, p_bonus, bonus_time
    
    level = lev
    life = lif
    score = sco
    
    gamewin_judge = 1
    
    pygame.init()
    pygame.mixer.init()
    
    bonusitem = pygame.mixer.Sound(os.path.join("sounds", "sfxBonusitem.wav"))
    collision = pygame.mixer.Sound(os.path.join("sounds", "sfxCollision.wav"))
    point = pygame.mixer.Sound(os.path.join("sounds", "sfxPoint.wav"))
    button = pygame.mixer.Sound(os.path.join("sounds", "sfxButton.wav"))
    click = pygame.mixer.Sound(os.path.join("sounds", "sfxClick.wav"))
    bgmLevel = pygame.mixer.Sound(os.path.join("sounds", "bgmLevel.wav"))
    
    button.set_volume(SFX)
    click.set_volume(SFX)  
    bonusitem.set_volume(SFX)
    collision.set_volume(SFX)
    point.set_volume(SFX)
    bgmLevel.set_volume(BGM)
    
    bgmLevel.play(-1)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    pygame.draw.line(background, (255, 255, 255), (0, windowHeight//10), (windowWidth, windowHeight//10), 1)
    whiteGear_pic = pygame.image.load(os.path.join("images", "whiteGear.png")).convert_alpha()
    whiteGear = pygame.transform.smoothscale(whiteGear_pic, (windowWidth//36, windowWidth//36))
    background.blit(whiteGear,(windowWidth*17//18, windowHeight//36))
    
    clock = pygame.time.Clock()
    fps = 60
    speed = windowWidth // fps // 2
    allsprite = pygame.sprite.Group()
    combo = 0
    
    brk = [None]*1000
    for i in range((position.height)*(position.width)):
        if random.random() <= p_bonus:
            bonus_num =  random.randint(1,4)
            brk[i] = brick.brick( i, windowWidth, windowHeight,bonus_num)
        else:
            brk[i] = brick.brick( i, windowWidth, windowHeight,0)
        k = int( (i) / position.width )
        j = int( (i) % position.width )
        if position.level[level-1][k][j] >= 1:
            allsprite.add(brk[i])
            brk[i].set_state(position.level[level-1][k][j])

            
    pad = paddle.paddle(windowWidth, windowHeight, speed)
    allsprite.add(pad)

    gameball = ball.ball(windowWidth, windowWidth, pad.tempX, pad.rect.y, speed)
    allsprite.add(gameball)
    
    score_board = scoreboard.scoreboard(windowWidth, windowHeight, life, score)
    allsprite.add(score_board)

    has_bonus = [False] * 5
    gameball.pos_on_pad = pad.paddleWidth//2 - gameball.radius//2
    btnclick = False
    mainLoop = True
    while mainLoop:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                mainLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    pad.left = True
                    pad.right = False
                elif event.key == pygame.K_RIGHT or event.key == ord('d') :
                    pad.right = True
                    pad.left = False

                if event.key == pygame.K_F11 and (windowWidth,windowHeight) in pygame.display.list_modes():
                    pygame.display.toggle_fullscreen()
                    full = not full

                if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == ord('w'):
                    if gameball.state == 'onpad' :
                        gameball.state = 'moving'
                        ball_leave_tick = pygame.time.get_ticks()
                        collision.play()

                if event.key == pygame.K_ESCAPE:
                    bgmLevel.stop()
                    click.play()
                    screen.fill((0,0,0))
                    pygame.display.update()

                    num = setting(screen)
                    if num == 1:
                        return lif, sco, False
                    elif num == 2:
                        return lif, sco, True
                    
                    speed = windowWidth // fps // 2

                    button.set_volume(SFX)
                    click.set_volume(SFX)  
                    bonusitem.set_volume(SFX)
                    collision.set_volume(SFX)
                    point.set_volume(SFX)
                    bgmLevel.set_volume(BGM)
                    
                    bgmLevel.play(-1)

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0, 0, 0))
                    pygame.draw.line(background, (255, 255, 255), (0, windowHeight//10), (windowWidth, windowHeight//10), 1)
                    background.blit(whiteGear,(windowWidth*17//18, windowHeight//36))
                    for sprite in allsprite:
                        sprite.change(windowWidth, windowHeight)
                        sprite.update()
                    allsprite.draw(screen)
                    pygame.display.update()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    pad.left = False
                elif event.key == pygame.K_RIGHT or event.key == ord('d') :
                    pad.right = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if windowWidth*17//18 <= mouse[0] <= (windowWidth*17//18 + windowWidth//36) and windowHeight//36 <= mouse[1] <= (windowHeight//36 + windowWidth//36):
                    btnclick = True

            elif event.type == pygame.MOUSEBUTTONUP:
                btnclick = False
                if windowWidth*17//18 <= mouse[0] <= (windowWidth*17//18 + windowWidth//36) and windowHeight//36 <= mouse[1] <= (windowHeight//36 + windowWidth//18):
                    bgmLevel.stop()
                    click.play()
                    screen.fill((0,0,0))
                    pygame.display.update()

                    num = setting(screen)
                    if num == 1:
                        return lif, sco, False
                    elif num == 2:
                        return lif, sco, True
                    
                    speed = windowWidth // fps // 2

                    button.set_volume(SFX)
                    click.set_volume(SFX)  
                    bonusitem.set_volume(SFX)
                    collision.set_volume(SFX)
                    point.set_volume(SFX)
                    bgmLevel.set_volume(BGM)
                    
                    bgmLevel.play(-1)

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0, 0, 0))
                    pygame.draw.line(background, (255, 255, 255), (0, windowHeight//10), (windowWidth, windowHeight//10), 1)
                    background.blit(whiteGear,(windowWidth*17//18, windowHeight//36))
                    for sprite in allsprite:
                        sprite.change(windowWidth, windowHeight)
                        sprite.update()
                    allsprite.draw(screen)
                    pygame.display.update()

        if not btnclick and windowWidth*17//18 <= mouse[0] <= (windowWidth*17//18 + windowWidth//36) and windowHeight//36 <= mouse[1] <= (windowHeight//36 + windowWidth//36):
            pygame.draw.rect(background, (0,0,0), (windowWidth*17//18, windowHeight//36, windowWidth//36, windowWidth//36))
            whiteGear = pygame.transform.smoothscale(whiteGear_pic, (windowWidth//24, windowWidth//24))
            background.blit(whiteGear, (windowWidth*15//16, windowHeight//51))
        else:
            pygame.draw.rect(background, (0,0,0), (windowWidth*15//16, windowHeight//51, windowWidth//24, windowWidth//24))
            whiteGear = pygame.transform.smoothscale(whiteGear_pic, (windowWidth//36, windowWidth//36))
            background.blit(whiteGear, (windowWidth*17//18, windowHeight//36))
 
        pygame.display.update()
        for i in range((position.height)*(position.width)):
            if brk[i].bonus != 0 and brk[i].state == 'dropping':
                brk[i].move()
            if pygame.sprite.collide_rect(pad,brk[i]) and allsprite.has(brk[i]):
                gameball.bonus_start_tick[brk[i].bonus] = pygame.time.get_ticks()
                has_bonus[brk[i].bonus] = True
                if brk[i].bonus == 1:
                    gameball.state_penetrate = True
                    gameball.penetrate()
                elif brk[i].bonus == 2:
                    gameball.state_sticky = True
                    pad.sticky(gameball.state_sticky)
                elif brk[i].bonus == 3:
                    pad.longer_paddle()
                elif brk[i].bonus == 4:
                    pad.shorter_paddle()
                allsprite.remove(brk[i])
            if brk[i].rect.y >= windowHeight:
                allsprite.remove(brk[i])
        if True in has_bonus:
            if pygame.time.get_ticks() - gameball.bonus_start_tick[1] >= bonus_time:
                gameball.state_penetrate = False
                gameball.penetrate()
                has_bonus[1] = False
            if pygame.time.get_ticks() - gameball.bonus_start_tick[2] >= bonus_time:
                gameball.state_sticky = False
                pad.sticky(gameball.state_sticky)
                has_bonus[2] = False
        
        
        if gameball.state == 'moving' :
            gameball.move()
            x = gameball.tempx+gameball.radius//2-pad.tempX-pad.paddleWidth/2
            if gameball.rect.x+gameball.dx*2 <= 0:
                gameball.collide("x")
                collision.play()

            elif gameball.rect.x+gameball.radius+gameball.dx*2 >= windowWidth:
                gameball.collide("x")
                collision.play()

            elif gameball.rect.y+gameball.dy*2 <= windowHeight // 10:
                gameball.collide("y")
                collision.play()

            elif gameball.rect.y+gameball.radius+gameball.dy*2 >= pad.rect.y and gameball.rect.y <= pad.rect.y and abs(x) <= pad.paddleWidth/2:
                if gameball.state_sticky == False:
                    if abs(x) > pad.paddleWidth/10:
                        angle = x/pad.paddleWidth*math.pi/3+math.pi/3
                        if gameball.angle > angle:
                            gameball.angle = math.pi/6*5-(math.pi/6*5-gameball.angle)*(angle-math.pi/6)/(math.pi/6*5-angle)
                        elif gameball.angle < angle:
                            gameball.angle = (gameball.angle-math.pi/6)*(math.pi/6*5-angle)/(angle-math.pi/6)+math.pi/6
                    gameball.collide("y")
                    
                elif gameball.state_sticky == True and (pygame.time.get_ticks() - ball_leave_tick) > 500:
                    gameball.state = 'onpad'
                    gameball.angle_reset()
                    x , y = pad.getxy()
                    gameball.pos_on_pad = gameball.rect.x - pad.rect.x
                    gameball.onpad(x , y)
                    
                
                collision.play()
                gameball.start_tick = pygame.time.get_ticks()
                combo = 0

            elif gameball.rect.y+gameball.radius+gameball.dy*2 >= windowHeight:
                life -= 1
                if life > 0:
                    score_board.losslife()
                    pad.reset()
                    gameball.reset()
                    gameball.start_tick = pygame.time.get_ticks()
                    combo = 0
                    x , y = pad.getxy()
                    gameball.pos_on_pad = pad.paddleWidth//2 - gameball.radius//2
                    gameball.onpad(x, y)
                    has_bonus = [False] * 5
                else:
                    bgmLevel.stop()
                    return life,score_board.get_score(),False

            for i in range((position.height)*(position.width)):
                if  brk[i].state == 'stationary' and allsprite.has(brk[i]) and gameball.rect.y+gameball.dy*2 <= brk[i].rect.y+brk[i].brickHeight and gameball.rect.y+gameball.radius+gameball.dy*2 >= brk[i].rect.y and gameball.rect.x+gameball.dx*2 <= brk[i].rect.x+brk[i].brickWidth and gameball.rect.x+gameball.radius+gameball.dx*2 >= brk[i].rect.x:
                    score_board.add(round(brk[i].point*(1+combo*0.5)))
                    brk[i].bonus_judge()
                    combo+=1
                    if brk[i].bonus == 0:
                        allsprite.remove(brk[i])
                    if gameball.state_penetrate == True:
                        pass
                    elif gameball.rect.x > brk[i].rect.x+brk[i].brickWidth or gameball.rect.x+gameball.radius < brk[i].rect.x:
                        gameball.collide("x")
                    else:
                        gameball.collide("y")
                    point.play()
            
        if gameball.state == 'onpad':
            x , y = pad.getxy()
            gameball.onpad(x, y)
        pad.move()
        
        screen.blit(background, (0, 0))
       
        for sprite in allsprite:
            sprite.update()
        allsprite.draw(screen)
        clock.tick(fps)
        pygame.display.update()
        
        for i in range((position.height)*(position.width)):
            if brk[i] in allsprite and brk[i].state == 'stationary':
                gamewin_judge = 0
                break
            
        if gamewin_judge == 1:
            bgmLevel.stop()
            return life,score_board.get_score(),True
        elif life >= 0:
            gamewin_judge = 1
    
    bgmLevel.stop()

    return life,score_board.get_score(),False


def setting(screen):

    global windowWidth, windowHeight, SFX, BGM, full

    pygame.init()
    pygame.mixer.init()
    
    soundplay = False
    button = pygame.mixer.Sound(os.path.join("sounds", "sfxButton.wav"))
    click = pygame.mixer.Sound(os.path.join("sounds", "sfxClick.wav"))
    bgmSetting = pygame.mixer.Sound(os.path.join("sounds", "bgmSetting.wav"))

    button.set_volume(SFX)
    click.set_volume(SFX)
    bgmSetting.set_volume(BGM)

    bgmSetting.play(-1)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//16)
    pause = font.render("PAUSE" , True,  (255, 255, 255),(0, 0, 0))
    
    resume_pic = pygame.image.load(os.path.join("images", "resume.png")).convert_alpha()
    restart_pic = pygame.image.load(os.path.join("images", "restart.png")).convert_alpha()
    option_pic = pygame.image.load(os.path.join("images", "option.png")).convert_alpha()
    exit_pic = pygame.image.load(os.path.join("images", "exit.png")).convert_alpha()

    resume_button = pygame.transform.smoothscale(resume_pic, (windowWidth//6, windowHeight//12))
    restart_button = pygame.transform.smoothscale(restart_pic, (windowWidth//6, windowHeight//12))
    option_button = pygame.transform.smoothscale(option_pic, (windowWidth//6, windowHeight//12))
    exit_button = pygame.transform.smoothscale(exit_pic, (windowWidth//6, windowHeight//12))
    
    background.blit(pause, (windowWidth*19//48, windowHeight//13))
    background.blit(resume_button,(windowWidth*5//12, windowHeight*4//15))
    background.blit(restart_button,(windowWidth*5//12, windowHeight*7//15))
    background.blit(option_button,(windowWidth*5//12, windowHeight*2//3))
    background.blit(exit_button, (windowWidth*5//12, windowHeight*13//15))

    btnclick = False
    mainloop = True
    while mainloop:
        
        screen.blit(background,(0,0))
        pygame.display.update()
        
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                mainloop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgmSetting.stop()
                    click.play()
                    mainloop = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                btnclick = True
                if windowWidth*4//10 <= mouse[0] <= (windowWidth*4//10 + windowWidth//5) and windowHeight//4 <= mouse[1] <= (windowHeight//4 + windowHeight*17//24):
                    pygame.draw.rect(background,(0,0,0), (windowWidth*4//10, windowHeight//4, windowWidth//5, windowHeight*17//24))
                    resume_button = pygame.transform.smoothscale(resume_pic, (windowWidth//6, windowHeight//12))
                    restart_button = pygame.transform.smoothscale(restart_pic, (windowWidth//6, windowHeight//12))
                    option_button = pygame.transform.smoothscale(option_pic, (windowWidth//6, windowHeight//12))
                    exit_button = pygame.transform.smoothscale(exit_pic, (windowWidth//6, windowHeight//12))

                    background.blit(resume_button, (windowWidth*5//12, windowHeight*4//15))
                    background.blit(restart_button, (windowWidth*5//12, windowHeight*7//15))
                    background.blit(option_button, (windowWidth*5//12, windowHeight*2//3))
                    background.blit(exit_button, (windowWidth*5//12, windowHeight*13//15))

            elif event.type == pygame.MOUSEBUTTONUP:
                btnclick = False
                if windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*4//15 <= mouse[1] <= (windowHeight*4//15 + windowHeight//12):
                    bgmSetting.stop()
                    click.play()
                    mainloop = False
                    
                elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*7//15 <= mouse[1] <= (windowHeight*7//15 + windowHeight//12):
                    bgmSetting.stop()
                    click.play()
                    return 2

                elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*2//3 <= mouse[1] <= (windowHeight*2//3 + windowHeight//12):
                    bgmSetting.stop()
                    click.play()
                    screen.fill((0,0,0))
                    pygame.display.update()
                    option(screen)

                    button.set_volume(SFX)
                    click.set_volume(SFX)
                    bgmSetting.set_volume(BGM)

                    bgmSetting.play(-1)

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0, 0, 0))
                    
                    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//16)
                    pause = font.render("PAUSE" , True,  (255, 255, 255),(0, 0, 0))

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0,0,0))

                    resume_button = pygame.transform.smoothscale(resume_pic, (windowWidth//6, windowHeight//12))
                    restart_button = pygame.transform.smoothscale(restart_pic, (windowWidth//6, windowHeight//12))
                    option_button = pygame.transform.smoothscale(option_pic, (windowWidth//6, windowHeight//12))
                    exit_button = pygame.transform.smoothscale(exit_pic, (windowWidth//6, windowHeight//12))

                    background.blit(pause, (windowWidth*19//48, windowHeight//13))
                    background.blit(resume_button,(windowWidth*5//12, windowHeight*4//15))
                    background.blit(restart_button,(windowWidth*5//12, windowHeight*7//15))
                    background.blit(option_button,(windowWidth*5//12, windowHeight*2//3))
                    background.blit(exit_button, (windowWidth*5//12, windowHeight*13//15))

                elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*13//15 <= mouse[1] <= (windowHeight*13//15 + windowHeight//12):
                    bgmSetting.stop()
                    click.play()
                    return 1

        screen.blit(background, (0,0))
        if not btnclick and windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*4//15 <= mouse[1] <= (windowHeight*4//15 + windowHeight//12):
            pygame.draw.rect(background, (0,0,0), (windowWidth*5//12, windowHeight*4//15, windowWidth//6, windowHeight//12))
            resume_button = pygame.transform.smoothscale(resume_pic, (windowWidth//5, windowHeight//10))
            background.blit(resume_button, (windowWidth*4//10, windowHeight*31//120))
            if not soundplay:
                button.play()
                soundplay = True

        elif not btnclick and windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*7//15 <= mouse[1] <= (windowHeight*7//15 + windowHeight//12):
            pygame.draw.rect(background, (0,0,0), (windowWidth*5//12, windowHeight*7//15, windowWidth//6, windowHeight//12))
            restart_button = pygame.transform.smoothscale(restart_pic, (windowWidth//5, windowHeight//10))
            background.blit(restart_button, (windowWidth*4//10, windowHeight*11//24))
            if not soundplay:
                button.play()
                soundplay = True

        elif not btnclick and windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*2//3 <= mouse[1] <= (windowHeight*2//3 + windowHeight//12):
            pygame.draw.rect(background, (0,0,0), (windowWidth*5//12, windowHeight*2//3, windowWidth//6, windowHeight//12))
            option_button = pygame.transform.smoothscale(option_pic, (windowWidth//5, windowHeight//10))
            background.blit(option_button, (windowWidth*4//10, windowHeight*79//120))
            if not soundplay:
                button.play()
                soundplay = True

        elif not btnclick and windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*13//15 <= mouse[1] <= (windowHeight*13//15 + windowHeight//12):
            pygame.draw.rect(background, (0,0,0), (windowWidth*5//12, windowHeight*13//15, windowWidth//6, windowHeight//12))
            exit_button = pygame.transform.smoothscale(exit_pic, (windowWidth//5, windowHeight//10))
            background.blit(exit_button, (windowWidth*4//10, windowHeight*103//120))
            if not soundplay:
                button.play()
                soundplay = True

        else:
            pygame.draw.rect(background,(0,0,0),(windowWidth*4//10,windowHeight//4,windowWidth//5, windowHeight*17//24))
            resume_button = pygame.transform.smoothscale(resume_pic, (windowWidth//6, windowHeight//12))
            restart_button = pygame.transform.smoothscale(restart_pic, (windowWidth//6, windowHeight//12))
            option_button = pygame.transform.smoothscale(option_pic, (windowWidth//6, windowHeight//12))
            exit_button = pygame.transform.smoothscale(exit_pic, (windowWidth//6, windowHeight//12))

            background.blit(resume_button,(windowWidth*5//12, windowHeight*4//15))
            background.blit(restart_button,(windowWidth*5//12, windowHeight*7//15))
            background.blit(option_button,(windowWidth*5//12, windowHeight*2//3))
            background.blit(exit_button, (windowWidth*5//12, windowHeight*13//15))

            soundplay = False
        
        pygame.display.update()
    bgmSetting.stop()
    return 3
    
def option(screen):

    global windowWidth, windowHeight, SFX, BGM, full

    dis = [1920, 1600, 1366, 1280, 960]

    pygame.init()
    pygame.mixer.init()

    button = pygame.mixer.Sound(os.path.join("sounds", "sfxButton.wav"))
    click = pygame.mixer.Sound(os.path.join("sounds", "sfxClick.wav"))
    bgmOption = pygame.mixer.Sound(os.path.join("sounds", "bgmOption.wav"))

    button.set_volume(SFX)
    click.set_volume(SFX)
    bgmOption.set_volume(BGM)

    bgmOption.play(-1)
    
    soundplay = False
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    arrow_pic = pygame.image.load(os.path.join("images", "arrow.png")).convert_alpha()
    right_pic = pygame.image.load(os.path.join("images", "right.png")).convert_alpha()
    left_pic = pygame.image.load(os.path.join("images", "left.png")).convert_alpha()
    grayright_pic = pygame.image.load(os.path.join("images", "grayright.png")).convert_alpha()
    grayleft_pic = pygame.image.load(os.path.join("images", "grayleft.png")).convert_alpha()
    check_pic = pygame.image.load(os.path.join("images", "check.png")).convert_alpha()

    arrow = pygame.transform.smoothscale(arrow_pic, (windowWidth//16, windowHeight//16))
    right = pygame.transform.smoothscale(right_pic, (windowWidth//32, windowHeight//32))
    left = pygame.transform.smoothscale(left_pic, (windowWidth//32, windowHeight//32))
    grayright = pygame.transform.smoothscale(grayright_pic, (windowWidth//32, windowHeight//32))
    grayleft = pygame.transform.smoothscale(grayleft_pic, (windowWidth//32, windowHeight//32))
    check = pygame.transform.smoothscale(check_pic, (windowWidth//24, windowHeight//12))

    titleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//16)
    option = titleFont.render("Option" , True,  (255, 255, 255),(0, 0, 0))
    

    subtitleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//24)
    resolution = subtitleFont.render("Resolution" , True,  (255, 255, 255),(0, 0, 0))
    volume = subtitleFont.render("Volume" , True,  (255, 255, 255),(0, 0, 0))
    fullscreen = subtitleFont.render("Fullscreen", True, (255, 255, 255),(0, 0, 0))

    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//32)
    res = [None]*5
    res[0] = font.render("1920x1080" , True,  (255, 255, 255),(0, 0, 0))
    res[1] = font.render("1600x900" , True,  (255, 255, 255),(0, 0, 0))
    res[2] = font.render("1366x768" , True,  (255, 255, 255),(0, 0, 0))
    res[3] = font.render("1280x720" , True,  (255, 255, 255),(0, 0, 0))
    res[4] = font.render("960x540" , True,  (255, 255, 255),(0, 0, 0))
    bgm = font.render("BGM" , True,  (255, 255, 255),(0, 0, 0))
    sfx = font.render("SFX" , True,  (255, 255, 255),(0, 0, 0))
    bgmPercent = font.render(str(round(BGM*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
    sfxPercent = font.render(str(round(SFX*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
    quit = font.render("QUIT" , True,  (255, 255, 255),(0, 0, 0))
    
    background.blit(option,(windowWidth*2//5, 0))
    background.blit(resolution, (windowWidth//8, windowHeight*3//16))
    for i in range(5):
        background.blit(res[i], (windowWidth//8, windowHeight*(i*2+5)//16))
        if dis[i] == windowWidth:
            background.blit(arrow, (windowWidth//24, windowHeight*(i*2+5.2)//16))
    background.blit(volume, (windowWidth*5//8, windowHeight*3//16))
    background.blit(bgm, (windowWidth*5//8, windowHeight*5//16))
    background.blit(sfx, (windowWidth*5//8, windowHeight*7//16))
    background.blit(bgmPercent, (windowWidth*13//16, windowHeight*5//16))
    background.blit(sfxPercent, (windowWidth*13//16, windowHeight*7//16))
    background.blit(left, (windowWidth*3//4, windowHeight*11//32))
    background.blit(right, (windowWidth*29//32, windowHeight*11//32))
    background.blit(left, (windowWidth*3//4, windowHeight*15//32))
    background.blit(right, (windowWidth*29//32, windowHeight*15//32))
    background.blit(fullscreen, (windowWidth*5//8, windowHeight*5//8))
    background.blit(quit, (windowWidth*15//32, windowHeight*7//8))
    
    screen.blit(background, (0,0))
    mainLoop = True
    while mainLoop:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bgmOption.stop()
                return True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgmOption.stop()
                    return False
                if event.key == pygame.K_F11 and (windowWidth,windowHeight) in pygame.display.list_modes():
                    pygame.display.toggle_fullscreen()
                    full = not full

            elif event.type == pygame.MOUSEBUTTONUP:
                if windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*5//16 <= mouse[1] <= windowHeight*13//32:
                    click.play()
                    windowWidth = 1920
                    windowHeight = windowWidth * 9 // 16
                    screen = pygame.display.set_mode((windowWidth, windowHeight))
                    if full:
                        if (windowWidth, windowHeight) in pygame.display.list_modes():
                            pygame.display.toggle_fullscreen()
                        else:
                            full = False
                    
                    arrow = pygame.transform.smoothscale(arrow_pic, (windowWidth//16, windowHeight//16))
                    right = pygame.transform.smoothscale(right_pic, (windowWidth//32, windowHeight//32))
                    left = pygame.transform.smoothscale(left_pic, (windowWidth//32, windowHeight//32))
                    grayright = pygame.transform.smoothscale(grayright_pic, (windowWidth//32, windowHeight//32))
                    grayleft = pygame.transform.smoothscale(grayleft_pic, (windowWidth//32, windowHeight//32))
                    check = pygame.transform.smoothscale(check_pic, (windowWidth//24, windowHeight//12))

                    titleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//16)
                    option = titleFont.render("Option" , True,  (255, 255, 255),(0, 0, 0))
    
                    subtitleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//24)
                    resolution = subtitleFont.render("Resolution" , True,  (255, 255, 255),(0, 0, 0))
                    volume = subtitleFont.render("Volume" , True,  (255, 255, 255),(0, 0, 0))
                    fullscreen = subtitleFont.render("Fullscreen", True, (255, 255, 255),(0, 0, 0))

                    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//32)
                    res = [None]*5
                    res[0] = font.render("1920x1080" , True,  (255, 255, 255),(0, 0, 0))
                    res[1] = font.render("1600x900" , True,  (255, 255, 255),(0, 0, 0))
                    res[2] = font.render("1366x768" , True,  (255, 255, 255),(0, 0, 0))
                    res[3] = font.render("1280x720" , True,  (255, 255, 255),(0, 0, 0))
                    res[4] = font.render("960x540" , True,  (255, 255, 255),(0, 0, 0))
                    bgm = font.render("BGM" , True,  (255, 255, 255),(0, 0, 0))
                    sfx = font.render("SFX" , True,  (255, 255, 255),(0, 0, 0))
                    bgmPercent = font.render(str(round(BGM*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    sfxPercent = font.render(str(round(SFX*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    quit = font.render("QUIT" , True,  (255, 255, 255),(0, 0, 0))

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0,0,0))
                    background.blit(option,(windowWidth*2//5, 0))
                    background.blit(resolution, (windowWidth//8, windowHeight*3//16))
                    for i in range(5):
                        background.blit(res[i], (windowWidth//8, windowHeight*(i*2+5)//16))
                        if dis[i] == windowWidth:
                            background.blit(arrow, (windowWidth//24, windowHeight*(i*2+5.2)//16))
                    background.blit(volume, (windowWidth*5//8, windowHeight*3//16))
                    background.blit(bgm, (windowWidth*5//8, windowHeight*5//16))
                    background.blit(sfx, (windowWidth*5//8, windowHeight*7//16))
                    background.blit(bgmPercent, (windowWidth*13//16, windowHeight*5//16))
                    background.blit(sfxPercent, (windowWidth*13//16, windowHeight*7//16))
                    background.blit(left, (windowWidth*3//4, windowHeight*11//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*11//32))
                    background.blit(left, (windowWidth*3//4, windowHeight*15//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*15//32))
                    background.blit(fullscreen, (windowWidth*5//8, windowHeight*5//8))
                    background.blit(quit, (windowWidth*15//32, windowHeight*7//8))
                
                elif windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*7//16 <= mouse[1] <= windowHeight*17//32:
                    click.play()
                    windowWidth = 1600
                    windowHeight = windowWidth * 9 // 16
                    screen = pygame.display.set_mode((windowWidth, windowHeight))
                    if full:
                        if (windowWidth, windowHeight) in pygame.display.list_modes():
                            pygame.display.toggle_fullscreen()
                        else:
                            full = False

                    arrow = pygame.transform.smoothscale(arrow_pic, (windowWidth//16, windowHeight//16))
                    right = pygame.transform.smoothscale(right_pic, (windowWidth//32, windowHeight//32))
                    left = pygame.transform.smoothscale(left_pic, (windowWidth//32, windowHeight//32))
                    grayright = pygame.transform.smoothscale(grayright_pic, (windowWidth//32, windowHeight//32))
                    grayleft = pygame.transform.smoothscale(grayleft_pic, (windowWidth//32, windowHeight//32))
                    check = pygame.transform.smoothscale(check_pic, (windowWidth//24, windowHeight//12))

                    titleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//16)
                    option = titleFont.render("Option" , True,  (255, 255, 255),(0, 0, 0))
    
                    subtitleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//24)
                    resolution = subtitleFont.render("Resolution" , True,  (255, 255, 255),(0, 0, 0))
                    volume = subtitleFont.render("Volume" , True,  (255, 255, 255),(0, 0, 0))
                    fullscreen = subtitleFont.render("Fullscreen", True, (255, 255, 255),(0, 0, 0))

                    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//32)
                    res = [None]*5
                    res[0] = font.render("1920x1080" , True,  (255, 255, 255),(0, 0, 0))
                    res[1] = font.render("1600x900" , True,  (255, 255, 255),(0, 0, 0))
                    res[2] = font.render("1366x768" , True,  (255, 255, 255),(0, 0, 0))
                    res[3] = font.render("1280x720" , True,  (255, 255, 255),(0, 0, 0))
                    res[4] = font.render("960x540" , True,  (255, 255, 255),(0, 0, 0))
                    bgm = font.render("BGM" , True,  (255, 255, 255),(0, 0, 0))
                    sfx = font.render("SFX" , True,  (255, 255, 255),(0, 0, 0))
                    bgmPercent = font.render(str(round(BGM*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    sfxPercent = font.render(str(round(SFX*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    quit = font.render("QUIT" , True,  (255, 255, 255),(0, 0, 0))

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0,0,0))
                    background.blit(option,(windowWidth*2//5, 0))
                    background.blit(resolution, (windowWidth//8, windowHeight*3//16))
                    for i in range(5):
                        background.blit(res[i], (windowWidth//8, windowHeight*(i*2+5)//16))
                        if dis[i] == windowWidth:
                            background.blit(arrow, (windowWidth//24, windowHeight*(i*2+5.2)//16))
                    background.blit(volume, (windowWidth*5//8, windowHeight*3//16))
                    background.blit(bgm, (windowWidth*5//8, windowHeight*5//16))
                    background.blit(sfx, (windowWidth*5//8, windowHeight*7//16))
                    background.blit(bgmPercent, (windowWidth*13//16, windowHeight*5//16))
                    background.blit(sfxPercent, (windowWidth*13//16, windowHeight*7//16))
                    background.blit(left, (windowWidth*3//4, windowHeight*11//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*11//32))
                    background.blit(left, (windowWidth*3//4, windowHeight*15//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*15//32))
                    background.blit(fullscreen, (windowWidth*5//8, windowHeight*5//8))
                    background.blit(quit, (windowWidth*15//32, windowHeight*7//8))
                elif windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*9//16 <= mouse[1] <= windowHeight*21//32:
                    click.play()
                    windowWidth = 1366
                    windowHeight = windowWidth * 9 // 16
                    screen = pygame.display.set_mode((windowWidth, windowHeight))
                    if full:
                        if (windowWidth, windowHeight) in pygame.display.list_modes():
                            pygame.display.toggle_fullscreen()
                        else:
                            full = False

                    arrow = pygame.transform.smoothscale(arrow_pic, (windowWidth//16, windowHeight//16))
                    right = pygame.transform.smoothscale(right_pic, (windowWidth//32, windowHeight//32))
                    left = pygame.transform.smoothscale(left_pic, (windowWidth//32, windowHeight//32))
                    grayright = pygame.transform.smoothscale(grayright_pic, (windowWidth//32, windowHeight//32))
                    grayleft = pygame.transform.smoothscale(grayleft_pic, (windowWidth//32, windowHeight//32))
                    check = pygame.transform.smoothscale(check_pic, (windowWidth//24, windowHeight//12))

                    titleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//16)
                    option = titleFont.render("Option" , True,  (255, 255, 255),(0, 0, 0))
    
                    subtitleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//24)
                    resolution = subtitleFont.render("Resolution" , True,  (255, 255, 255),(0, 0, 0))
                    volume = subtitleFont.render("Volume" , True,  (255, 255, 255),(0, 0, 0))
                    fullscreen = subtitleFont.render("Fullscreen", True, (255, 255, 255),(0, 0, 0))

                    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//32)
                    res = [None]*5
                    res[0] = font.render("1920x1080" , True,  (255, 255, 255),(0, 0, 0))
                    res[1] = font.render("1600x900" , True,  (255, 255, 255),(0, 0, 0))
                    res[2] = font.render("1366x768" , True,  (255, 255, 255),(0, 0, 0))
                    res[3] = font.render("1280x720" , True,  (255, 255, 255),(0, 0, 0))
                    res[4] = font.render("960x540" , True,  (255, 255, 255),(0, 0, 0))
                    bgm = font.render("BGM" , True,  (255, 255, 255),(0, 0, 0))
                    sfx = font.render("SFX" , True,  (255, 255, 255),(0, 0, 0))
                    bgmPercent = font.render(str(round(BGM*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    sfxPercent = font.render(str(round(SFX*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    quit = font.render("QUIT" , True,  (255, 255, 255),(0, 0, 0))

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0,0,0))
                    background.blit(option,(windowWidth*2//5, 0))
                    background.blit(resolution, (windowWidth//8, windowHeight*3//16))
                    for i in range(5):
                        background.blit(res[i], (windowWidth//8, windowHeight*(i*2+5)//16))
                        if dis[i] == windowWidth:
                            background.blit(arrow, (windowWidth//24, windowHeight*(i*2+5.2)//16))
                    background.blit(volume, (windowWidth*5//8, windowHeight*3//16))
                    background.blit(bgm, (windowWidth*5//8, windowHeight*5//16))
                    background.blit(sfx, (windowWidth*5//8, windowHeight*7//16))
                    background.blit(bgmPercent, (windowWidth*13//16, windowHeight*5//16))
                    background.blit(sfxPercent, (windowWidth*13//16, windowHeight*7//16))
                    background.blit(left, (windowWidth*3//4, windowHeight*11//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*11//32))
                    background.blit(left, (windowWidth*3//4, windowHeight*15//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*15//32))
                    background.blit(fullscreen, (windowWidth*5//8, windowHeight*5//8))
                    background.blit(quit, (windowWidth*15//32, windowHeight*7//8))

                elif windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*11//16 <= mouse[1] <= windowHeight*25//32:
                    click.play()
                    windowWidth = 1280
                    windowHeight = windowWidth * 9 // 16
                    screen = pygame.display.set_mode((windowWidth, windowHeight))
                    if full:
                        if (windowWidth, windowHeight) in pygame.display.list_modes():
                            pygame.display.toggle_fullscreen()
                        else:
                            full = False

                    arrow = pygame.transform.smoothscale(arrow_pic, (windowWidth//16, windowHeight//16))
                    right = pygame.transform.smoothscale(right_pic, (windowWidth//32, windowHeight//32))
                    left = pygame.transform.smoothscale(left_pic, (windowWidth//32, windowHeight//32))
                    grayright = pygame.transform.smoothscale(grayright_pic, (windowWidth//32, windowHeight//32))
                    grayleft = pygame.transform.smoothscale(grayleft_pic, (windowWidth//32, windowHeight//32))
                    check = pygame.transform.smoothscale(check_pic, (windowWidth//24, windowHeight//12))

                    titleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//16)
                    option = titleFont.render("Option" , True,  (255, 255, 255),(0, 0, 0))
    
                    subtitleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//24)
                    resolution = subtitleFont.render("Resolution" , True,  (255, 255, 255),(0, 0, 0))
                    volume = subtitleFont.render("Volume" , True,  (255, 255, 255),(0, 0, 0))
                    fullscreen = subtitleFont.render("Fullscreen", True, (255, 255, 255),(0, 0, 0))

                    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//32)
                    res = [None]*5
                    res[0] = font.render("1920x1080" , True,  (255, 255, 255),(0, 0, 0))
                    res[1] = font.render("1600x900" , True,  (255, 255, 255),(0, 0, 0))
                    res[2] = font.render("1366x768" , True,  (255, 255, 255),(0, 0, 0))
                    res[3] = font.render("1280x720" , True,  (255, 255, 255),(0, 0, 0))
                    res[4] = font.render("960x540" , True,  (255, 255, 255),(0, 0, 0))
                    bgm = font.render("BGM" , True,  (255, 255, 255),(0, 0, 0))
                    sfx = font.render("SFX" , True,  (255, 255, 255),(0, 0, 0))
                    bgmPercent = font.render(str(round(BGM*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    sfxPercent = font.render(str(round(SFX*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    quit = font.render("QUIT" , True,  (255, 255, 255),(0, 0, 0))

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0,0,0))
                    background.blit(option,(windowWidth*2//5, 0))
                    background.blit(resolution, (windowWidth//8, windowHeight*3//16))
                    for i in range(5):
                        background.blit(res[i], (windowWidth//8, windowHeight*(i*2+5)//16))
                        if dis[i] == windowWidth:
                            background.blit(arrow, (windowWidth//24, windowHeight*(i*2+5.2)//16))
                    background.blit(volume, (windowWidth*5//8, windowHeight*3//16))
                    background.blit(bgm, (windowWidth*5//8, windowHeight*5//16))
                    background.blit(sfx, (windowWidth*5//8, windowHeight*7//16))
                    background.blit(bgmPercent, (windowWidth*13//16, windowHeight*5//16))
                    background.blit(sfxPercent, (windowWidth*13//16, windowHeight*7//16))
                    background.blit(left, (windowWidth*3//4, windowHeight*11//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*11//32))
                    background.blit(left, (windowWidth*3//4, windowHeight*15//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*15//32))
                    background.blit(fullscreen, (windowWidth*5//8, windowHeight*5//8))
                    background.blit(quit, (windowWidth*15//32, windowHeight*7//8))

                elif windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*13//16 <= mouse[1] <= windowHeight*29//32:
                    click.play()
                    windowWidth = 960
                    windowHeight = windowWidth * 9 // 16
                    screen = pygame.display.set_mode((windowWidth, windowHeight))
                    if full:
                        if (windowWidth, windowHeight) in pygame.display.list_modes():
                            pygame.display.toggle_fullscreen()
                        else:
                            full = False

                    arrow = pygame.transform.smoothscale(arrow_pic, (windowWidth//16, windowHeight//16))
                    right = pygame.transform.smoothscale(right_pic, (windowWidth//32, windowHeight//32))
                    left = pygame.transform.smoothscale(left_pic, (windowWidth//32, windowHeight//32))
                    grayright = pygame.transform.smoothscale(grayright_pic, (windowWidth//32, windowHeight//32))
                    grayleft = pygame.transform.smoothscale(grayleft_pic, (windowWidth//32, windowHeight//32))
                    check = pygame.transform.smoothscale(check_pic, (windowWidth//24, windowHeight//12))

                    titleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//16)
                    option = titleFont.render("Option" , True,  (255, 255, 255),(0, 0, 0))
    
                    subtitleFont = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//24)
                    resolution = subtitleFont.render("Resolution" , True,  (255, 255, 255),(0, 0, 0))
                    volume = subtitleFont.render("Volume" , True,  (255, 255, 255),(0, 0, 0))
                    fullscreen = subtitleFont.render("Fullscreen", True, (255, 255, 255),(0, 0, 0))

                    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth//32)
                    res = [None]*5
                    res[0] = font.render("1920x1080" , True,  (255, 255, 255),(0, 0, 0))
                    res[1] = font.render("1600x900" , True,  (255, 255, 255),(0, 0, 0))
                    res[2] = font.render("1366x768" , True,  (255, 255, 255),(0, 0, 0))
                    res[3] = font.render("1280x720" , True,  (255, 255, 255),(0, 0, 0))
                    res[4] = font.render("960x540" , True,  (255, 255, 255),(0, 0, 0))
                    bgm = font.render("BGM" , True,  (255, 255, 255),(0, 0, 0))
                    sfx = font.render("SFX" , True,  (255, 255, 255),(0, 0, 0))
                    bgmPercent = font.render(str(round(BGM*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    sfxPercent = font.render(str(round(SFX*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                    quit = font.render("QUIT" , True,  (255, 255, 255),(0, 0, 0))

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0,0,0))
                    background.blit(option,(windowWidth*2//5, 0))
                    background.blit(resolution, (windowWidth//8, windowHeight*3//16))
                    for i in range(5):
                        background.blit(res[i], (windowWidth//8, windowHeight*(i*2+5)//16))
                        if dis[i] == windowWidth:
                            background.blit(arrow, (windowWidth//24, windowHeight*(i*2+5.2)//16))
                    background.blit(volume, (windowWidth*5//8, windowHeight*3//16))
                    background.blit(bgm, (windowWidth*5//8, windowHeight*5//16))
                    background.blit(sfx, (windowWidth*5//8, windowHeight*7//16))
                    background.blit(bgmPercent, (windowWidth*13//16, windowHeight*5//16))
                    background.blit(sfxPercent, (windowWidth*13//16, windowHeight*7//16))
                    background.blit(left, (windowWidth*3//4, windowHeight*11//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*11//32))
                    background.blit(left, (windowWidth*3//4, windowHeight*15//32))
                    background.blit(right, (windowWidth*29//32, windowHeight*15//32))
                    background.blit(fullscreen, (windowWidth*5//8, windowHeight*5//8))
                    background.blit(quit, (windowWidth*15//32, windowHeight*7//8))

                elif windowWidth*3//4 <= mouse[0] <= windowWidth*25//32 and windowHeight*11//32 <= mouse[1] <= windowHeight*3//8:
                    if BGM > 0.01:
                        BGM -= 0.05
                        bgmPercent = font.render(str(round(BGM*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                        pygame.draw.rect(background, (0,0,0), (windowWidth*13//16, windowHeight*5//16,windowWidth*3//32,windowHeight//8))
                        background.blit(bgmPercent, (windowWidth*13//16, windowHeight*5//16))
                        bgmOption.set_volume(BGM)
                        click.play()

                elif windowWidth*29//32 <= mouse[0] <= windowWidth*15//16 and windowHeight*11//32 <= mouse[1] <= windowHeight*3//8:
                    if BGM < 0.99:
                        BGM += 0.05
                        bgmPercent = font.render(str(round(BGM*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                        pygame.draw.rect(background, (0,0,0), (windowWidth*13//16, windowHeight*5//16,windowWidth*3//32,windowHeight//8))
                        background.blit(bgmPercent, (windowWidth*13//16, windowHeight*5//16))
                        bgmOption.set_volume(BGM)
                        click.play()

                elif windowWidth*3//4 <= mouse[0] <= windowWidth*25//32 and windowHeight*15//32 <= mouse[1] <= windowHeight//2:
                    if SFX > 0.01:
                        SFX -= 0.05
                        sfxPercent = font.render(str(round(SFX*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                        pygame.draw.rect(background, (0,0,0), (windowWidth*13//16, windowHeight*7//16,windowWidth*3//32,windowHeight//8))
                        background.blit(sfxPercent, (windowWidth*13//16, windowHeight*7//16))
                        button.set_volume(SFX)
                        click.set_volume(SFX)
                        click.play()

                elif windowWidth*29//32 <= mouse[0] <= windowWidth*15//16 and windowHeight*15//32 <= mouse[1] <= windowHeight//2:
                    if SFX < 0.99:
                        SFX += 0.05
                        sfxPercent = font.render(str(round(SFX*100))+"%" , True,  (255, 255, 255),(0, 0, 0))
                        pygame.draw.rect(background, (0,0,0), (windowWidth*13//16, windowHeight*7//16,windowWidth*3//32,windowHeight//8))
                        background.blit(sfxPercent, (windowWidth*13//16, windowHeight*7//16))
                        button.set_volume(SFX)
                        click.set_volume(SFX)
                        click.play()

                elif windowWidth*5//8 <= mouse[0] <= windowWidth*15//16 and windowHeight*5//8 <= mouse[1] <= windowHeight*3//4:
                    if (windowWidth,windowHeight) in pygame.display.list_modes():
                        pygame.display.toggle_fullscreen()
                        full = not full
                    click.play()

                elif windowWidth*15//32 <= mouse[0] <= windowWidth*9//16 and windowHeight*7//8 <= mouse[1] <= windowHeight*31//32:
                    click.play()
                    bgmOption.stop()
                    return False

        
        if full:
            check = pygame.transform.smoothscale(check_pic, (windowWidth//24, windowHeight//12))
        else:
            check.fill((0,0,0))
        
        background.blit(check, (windowWidth*7//8, windowHeight*5//8))
        pygame.draw.rect(background, (255,255,255), (windowWidth*7//8, windowHeight*21//32, windowHeight//16, windowHeight//16), 2)

        if windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*5//16 <= mouse[1] <= windowHeight*13//32:
            res[0] = font.render("1920x1080" , True,  (150, 150, 150),(0, 0, 0))
            background.blit(res[0], (windowWidth//8, windowHeight*5//16))
            if not soundplay:
                button.play()
                soundplay = True
        
        elif windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*7//16 <= mouse[1] <= windowHeight*17//32:
            res[1] = font.render("1600x900" , True,  (150, 150, 150),(0, 0, 0))
            background.blit(res[1], (windowWidth//8, windowHeight*7//16))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*9//16 <= mouse[1] <= windowHeight*21//32:
            res[2] = font.render("1366x768" , True,  (150, 150, 150),(0, 0, 0))
            background.blit(res[2], (windowWidth//8, windowHeight*9//16))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*11//16 <= mouse[1] <= windowHeight*25//32:
            res[3] = font.render("1280x720" , True,  (150, 150, 150),(0, 0, 0))
            background.blit(res[3], (windowWidth//8, windowHeight*11//16))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth//24 <= mouse[0] <= windowWidth*3//8 and windowHeight*13//16 <= mouse[1] <= windowHeight*29//32:
            res[4] = font.render("960x540" , True,  (150, 150, 150),(0, 0, 0))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth*3//4 <= mouse[0] <= windowWidth*25//32 and windowHeight*11//32 <= mouse[1] <= windowHeight*3//8:
            background.blit(grayleft, (windowWidth*3//4, windowHeight*11//32))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth*29//32 <= mouse[0] <= windowWidth*15//16 and windowHeight*11//32 <= mouse[1] <= windowHeight*3//8:
            background.blit(grayright, (windowWidth*29//32, windowHeight*11//32))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth*3//4 <= mouse[0] <= windowWidth*25//32 and windowHeight*15//32 <= mouse[1] <= windowHeight//2:
            background.blit(grayleft, (windowWidth*3//4, windowHeight*15//32))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth*29//32 <= mouse[0] <= windowWidth*15//16 and windowHeight*15//32 <= mouse[1] <= windowHeight//2:
            background.blit(grayright, (windowWidth*29//32, windowHeight*15//32))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth*5//8 <= mouse[0] <= windowWidth*15//16 and windowHeight*5//8 <= mouse[1] <= windowHeight*3//4:
            fullscreen = subtitleFont.render("Fullscreen" , True,  (150, 150, 150),(0, 0, 0))
            pygame.draw.rect(background, (150,150,150), (windowWidth*7//8, windowHeight*21//32, windowHeight//16, windowHeight//16), 2)
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth*15//32 <= mouse[0] <= windowWidth*9//16 and windowHeight*7//8 <= mouse[1] <= windowHeight*31//32:
            quit = font.render("QUIT" , True,  (150, 150, 150),(0, 0, 0))
            if not soundplay:
                button.play()
                soundplay = True

        else:
            res[0] = font.render("1920x1080" , True,  (255, 255, 255),(0, 0, 0))
            res[1] = font.render("1600x900" , True,  (255, 255, 255),(0, 0, 0))
            res[2] = font.render("1366x768" , True,  (255, 255, 255),(0, 0, 0))
            res[3] = font.render("1280x720" , True,  (255, 255, 255),(0, 0, 0))
            res[4] = font.render("960x540" , True,  (255, 255, 255),(0, 0, 0))
            quit = font.render("QUIT" , True,  (255, 255, 255),(0, 0, 0))
            fullscreen = subtitleFont.render("Fullscreen", True, (255, 255, 255),(0, 0, 0))
            soundplay = False

            background.blit(left, (windowWidth*3//4, windowHeight*11//32))
            background.blit(right, (windowWidth*29//32, windowHeight*11//32))
            background.blit(left, (windowWidth*3//4, windowHeight*15//32))
            background.blit(right, (windowWidth*29//32, windowHeight*15//32))

            

        for i in range(5):
            background.blit(res[i], (windowWidth//8, windowHeight*(i*2+5)//16))
            if dis[i] == windowWidth:
                background.blit(arrow, (windowWidth//24, windowHeight*(i*2+5.2)//16))
        
        background.blit(fullscreen, (windowWidth*5//8, windowHeight*5//8))
        background.blit(quit, (windowWidth*15//32, windowHeight*7//8))
        
        screen.blit(background, (0,0))
        pygame.display.update()

    bgmOption.stop()
    return False


def main():
    global windowWidth, windowHeight, SFX, BGM, full

    total_level = 10
    current_level = 1
    current_life = 5
    current_score = 0
    
    
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight))

    button = pygame.mixer.Sound(os.path.join("sounds", "sfxButton.wav"))
    click = pygame.mixer.Sound(os.path.join("sounds", "sfxClick.wav"))
    bgmTitle = pygame.mixer.Sound(os.path.join("sounds", "bgmTitle.wav"))

    button.set_volume(SFX)
    click.set_volume(SFX)
    bgmTitle.set_volume(BGM)
    
    bgmTitle.play(-1)

    soundplay = False

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth // 12)
    breakout = font.render("Breakout" , True,  (255, 255, 255),(0, 0, 0))
    background.blit(breakout,(windowWidth//3,windowHeight//12))
    
    start_button_pic = pygame.image.load(os.path.join("images", "start.png")).convert_alpha()     
    start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//6, windowHeight//12))
    background.blit(start_button,(windowWidth*5//12,windowHeight*13//30))
    
    option_button_pic = pygame.image.load(os.path.join("images", "option.png")).convert_alpha()     
    option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//6, windowHeight//12))
    background.blit(option_button,(windowWidth*5//12,windowHeight*19//30))
    
    exit_button_pic = pygame.image.load(os.path.join("images", "exit.png")).convert_alpha()     
    exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//6, windowHeight//12))
    background.blit(exit_button,(windowWidth*5//12,windowHeight*5//6))
   
    
    screen.blit(background, (0,0))
    
    btnclick = False
    mainLoop = True
    while mainLoop:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainLoop = False
                if event.key == pygame.K_F11 and (windowWidth,windowHeight) in pygame.display.list_modes():
                    pygame.display.toggle_fullscreen()
                    full = not full
                
                if event.key == pygame.K_LSHIFT:
                    current_level += 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if windowWidth*4//10 <= mouse[0] <= (windowWidth*4//10 + windowWidth//5) and windowHeight*17//40 <= mouse[1] <= (windowHeight*17//40 + windowHeight//2):
                    btnclick = True
                    pygame.draw.rect(background,(0,0,0),(windowWidth*4//10,windowHeight*17//40,windowWidth//5, windowHeight//2))
                    start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//6, windowHeight//12))
                    background.blit(start_button,(windowWidth*5//12,windowHeight*13//30))
                    option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//6, windowHeight//12))
                    background.blit(option_button,(windowWidth*5//12,windowHeight*19//30))
                    exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//6, windowHeight//12))

                    background.blit(exit_button,(windowWidth*5//12,windowHeight*5//6))

            elif event.type == pygame.MOUSEBUTTONUP:
                btnclick = False
                if windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*13//30 <= mouse[1] <= (windowHeight*13//30 + windowHeight//12):
                    click.play()
                    bgmTitle.stop()
                    game_judge = True
                    while game_judge:
                        
                        screen.fill((0,0,0))
                        screen.blit(font.render("Level %s"%current_level , True,  (255, 255, 255),(0, 0, 0)),(windowWidth//3,windowHeight//3)) 
                        pygame.display.update()
                        pygame.time.wait(1000)

                        score = current_score
                        current_life,current_score,game_judge = gameloop(screen,current_level,current_life,current_score)
                       
                        if game_judge and current_life > 0 and score == current_score:
                            pass

                        elif game_judge and current_level < total_level:
                            current_level += 1

                        elif game_judge and current_level == total_level:
                            screen.fill((0,0,0))
                            font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth // 12)
                            screen.blit(font.render("Congratulation" , True,  (255, 255, 255),(0, 0, 0)),(windowWidth//3,windowHeight//3)) 
                            pygame.display.update()
                            pygame.time.wait(2000)
                            current_level = 1
                            current_life = 5
                            current_score = 0
                            game_judge = False
                            
                            button.set_volume(SFX)
                            click.set_volume(SFX)
                            bgmTitle.set_volume(BGM)

                            bgmTitle.play(-1)

                            background = pygame.Surface(screen.get_size())
                            background = background.convert()
                            background.fill((0,0,0))

                            font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth // 12)
                            breakout = font.render("Breakout" , True,  (255, 255, 255),(0, 0, 0))
                            start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//6, windowHeight//12))
                            option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//6, windowHeight//12))
                            exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//6, windowHeight//12))
                            
                            background.blit(breakout,(windowWidth//3,windowHeight//12))
                            background.blit(start_button,(windowWidth*5//12,windowHeight*13//30))
                            background.blit(option_button,(windowWidth*5//12,windowHeight*19//30))
                            background.blit(exit_button,(windowWidth*5//12,windowHeight*5//6))

                        elif current_life < 1:
                            screen.fill((0,0,0))
                            font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth // 12)
                            screen.blit(font.render("You lose" , True,  (255, 255, 255),(0, 0, 0)),(windowWidth//3,windowHeight//3)) 
                            pygame.display.update()
                            pygame.time.wait(2000)
                            current_level = 1
                            current_life = 5
                            current_score = 0
                            game_judge = False
                            
                            button.set_volume(SFX)
                            click.set_volume(SFX)
                            bgmTitle.set_volume(BGM)

                            bgmTitle.play(-1)

                            background = pygame.Surface(screen.get_size())
                            background = background.convert()
                            background.fill((0,0,0))

                            font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth // 12)
                            breakout = font.render("Breakout" , True,  (255, 255, 255),(0, 0, 0))
                            start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//6, windowHeight//12))
                            option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//6, windowHeight//12))
                            exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//6, windowHeight//12))
                            
                            background.blit(breakout,(windowWidth//3,windowHeight//12))
                            background.blit(start_button,(windowWidth*5//12,windowHeight*13//30))
                            background.blit(option_button,(windowWidth*5//12,windowHeight*19//30))
                            background.blit(exit_button,(windowWidth*5//12,windowHeight*5//6))

                        elif not game_judge:
                            current_level = 1
                            current_life = 5
                            current_score = 0
                            
                            button.set_volume(SFX)
                            click.set_volume(SFX)
                            bgmTitle.set_volume(BGM)

                            bgmTitle.play(-1)

                            background = pygame.Surface(screen.get_size())
                            background = background.convert()
                            background.fill((0,0,0))

                            font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth // 12)
                            breakout = font.render("Breakout" , True,  (255, 255, 255),(0, 0, 0))
                            start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//6, windowHeight//12))
                            option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//6, windowHeight//12))
                            exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//6, windowHeight//12))
                            
                            background.blit(breakout,(windowWidth//3,windowHeight//12))
                            background.blit(start_button,(windowWidth*5//12,windowHeight*13//30))
                            background.blit(option_button,(windowWidth*5//12,windowHeight*19//30))
                            background.blit(exit_button,(windowWidth*5//12,windowHeight*5//6))
                            
                        
                elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*19//30 <= mouse[1] <= (windowHeight*19//30 + windowHeight//12):
                    click.play()
                    bgmTitle.stop()
                    screen.fill((0,0,0))
                    pygame.display.update()
                    if option(screen):
                        return
                    
                    button.set_volume(SFX)
                    click.set_volume(SFX)
                    bgmTitle.set_volume(BGM)

                    bgmTitle.play(-1)

                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((0,0,0))

                    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), windowWidth // 12)
                    breakout = font.render("Breakout" , True,  (255, 255, 255),(0, 0, 0))
                    start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//6, windowHeight//12))
                    option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//6, windowHeight//12))
                    exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//6, windowHeight//12))
                    
                    background.blit(breakout,(windowWidth//3,windowHeight//12))
                    background.blit(start_button,(windowWidth*5//12,windowHeight*13//30))
                    background.blit(option_button,(windowWidth*5//12,windowHeight*19//30))
                    background.blit(exit_button,(windowWidth*5//12,windowHeight*5//6))

                elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*5//6 <= mouse[1] <= (windowHeight*5//6 + windowHeight//12):
                    mainLoop = False


        screen.blit(background, (0,0))
        if not btnclick and windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*13//30 <= mouse[1] <= (windowHeight*13//30 + windowHeight//12):
            pygame.draw.rect(background, (0,0,0), (windowWidth*5//12, windowHeight*13//30, windowWidth//6, windowHeight//12))
            start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//5, windowHeight//10))
            background.blit(start_button, (windowWidth*4//10, windowHeight*17//40))
            if not soundplay:
                button.play()
                soundplay = True

        elif not btnclick and windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*19//30 <= mouse[1] <= (windowHeight*19//30 + windowHeight//12):
            pygame.draw.rect(background, (0,0,0), (windowWidth*5//12, windowHeight*19//30, windowWidth//6, windowHeight//12))
            option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//5, windowHeight//10))
            background.blit(option_button, (windowWidth*4//10, windowHeight*5//8))
            if not soundplay:
                button.play()
                soundplay = True

        elif not btnclick and windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*5//6 <= mouse[1] <= (windowHeight*5//6 + windowHeight//12):
            pygame.draw.rect(background, (0,0,0), (windowWidth*5//12, windowHeight*5//6, windowWidth//6, windowHeight//12))
            exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//5, windowHeight//10))
            background.blit(exit_button, (windowWidth*4//10, windowHeight*33//40))
            if not soundplay:
                button.play()
                soundplay = True

        else:
            pygame.draw.rect(background,(0,0,0),(windowWidth*4//10,windowHeight*17//40,windowWidth//5, windowHeight//2))
            start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//6, windowHeight//12))
            background.blit(start_button,(windowWidth*5//12,windowHeight*13//30))
            option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//6, windowHeight//12))
            background.blit(option_button,(windowWidth*5//12,windowHeight*19//30))
            exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//6, windowHeight//12))
            background.blit(exit_button,(windowWidth*5//12,windowHeight*5//6))
            soundplay = False
        


        pygame.display.update()
    
    if full:
        pygame.display.toggle_fullscreen()

    pygame.mixer.quit()
    pygame.quit()


if __name__ == "__main__":
    main()