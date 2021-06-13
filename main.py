import pygame, math , os
import ball, brick, paddle, position, scoreboard

def gameloop(lev,lif,sco,vol):
    level = lev
    life = lif
    score = sco
    volume = vol
    
    gamewin_judge = 1
    windowWidth = 960
    windowHeight = windowWidth * 9 // 16
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight), pygame.SCALED)
    
    bonusitem = pygame.mixer.Sound(os.path.join("sounds", "bonusitem.wav"))
    collision = pygame.mixer.Sound(os.path.join("sounds", "collision.wav"))
    shoot = pygame.mixer.Sound(os.path.join("sounds", "shoot.wav"))

    bonusitem.set_volume(volume)
    collision.set_volume(volume)
    shoot.set_volume(volume)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    pygame.draw.line(background, (255, 255, 255), (0, windowHeight//10), (windowWidth, windowHeight//10), 1)
    

    clock = pygame.time.Clock()
    fps = 60
    speed = windowWidth // fps // 2
    allsprite = pygame.sprite.Group()
    combo = 0
    
    brk = [None]*1000
    for i in range((position.height)*(position.width)):
        brk[i] = brick.brick( i, windowWidth, windowHeight)
        k = int( (i) / position.width )
        j = int( (i) % position.width )
        if position.level[level-1][k][j] == 1:
            allsprite.add(brk[i])
            
    pad = paddle.paddle(windowWidth, windowHeight, speed)
    allsprite.add(pad)

    gameball = ball.ball(windowWidth, windowWidth, pad.tempX, pad.rect.y, speed)
    allsprite.add(gameball)
    
    score_board = scoreboard.scoreboard(windowWidth, windowHeight, life, score)
    allsprite.add(score_board)
    
    
    mainLoop = True
    while mainLoop:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    pad.left = True
                    pad.right = False
                elif event.key == pygame.K_RIGHT or event.key == ord('d') :
                    pad.right = True
                    pad.left = False

                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                    
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    if gameball.state == 'onpad':
                        gameball.state = 'moving'
                        shoot.play()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    pad.left = False
                elif event.key == pygame.K_RIGHT or event.key == ord('d') :
                    pad.right = False
                    
        if gameball.state == 'moving':
            gameball.move()
            x = gameball.rect.x+gameball.dx*2-pad.rect.x-pad.paddleWidth/2
            if gameball.rect.x+gameball.dx*2 <= 0:
                gameball.collide("x")
                collision.play()

            elif gameball.rect.x+gameball.radius+gameball.dx*2 >= windowWidth:
                gameball.collide("x")
                collision.play()

            elif gameball.rect.y+gameball.dy*2 <= windowHeight // 10:
                gameball.collide("y")
                collision.play()

            elif gameball.rect.y+gameball.radius+gameball.dy*2 >= pad.rect.y and gameball.rect.y <= pad.rect.y+pad.paddleHeight and abs(x) <= pad.paddleWidth/2:
                if abs(x) > pad.paddleWidth/10:
                    angle = x/pad.paddleWidth*math.pi/3+math.pi/3
                    if gameball.angle > angle:
                        gameball.angle = math.pi/6*5-(math.pi/6*5-gameball.angle)*(angle-math.pi/6)/(math.pi/6*5-angle)
                    elif gameball.angle < angle:
                        gameball.angle = (gameball.angle-math.pi/6)*(math.pi/6*5-angle)/(angle-math.pi/6)+math.pi/6
                gameball.collide("y")
                collision.play()
                gameball.start_tick = pygame.time.get_ticks()
                combo = 0
        
            elif gameball.rect.y+gameball.radius+gameball.dy*2 >= windowHeight:
                if life > 1:
                    life -= 1
                    score_board.losslife()
                    gameball.state = 'onpad'
                    gameball.start_tick = pygame.time.get_ticks()
                    combo = 0
                else:
                    return life,score_board.get_score(),False
            for i in range((position.height)*(position.width)):
                if  allsprite.has(brk[i]) and gameball.rect.y+gameball.dy*2 <= brk[i].rect.y+brk[i].brickHeight and gameball.rect.y+gameball.radius+gameball.dy*2 >= brk[i].rect.y and gameball.rect.x+gameball.dx*2 <= brk[i].rect.x+brk[i].brickWidth and gameball.rect.x+gameball.radius+gameball.dx*2 >= brk[i].rect.x:
                    score_board.add(round(brk[i].point*(1+combo*0.5)))
                    allsprite.remove(brk[i])
                    combo+=1
                    if gameball.rect.x > brk[i].rect.x+brk[i].brickWidth or gameball.rect.x+gameball.radius < brk[i].rect.x:
                        gameball.collide("x")
                        collision.play()
                    else:
                        gameball.collide("y")
                        collision.play()
            
        elif gameball.state == 'onpad':
            x, y = pad.getxy()
            x +=  pad.paddleWidth // 2
            gameball.onpad(x, y)
        
        pad.move()

        screen.blit(background, (0, 0))
       
        for sprite in allsprite:
            sprite.update()
        allsprite.draw(screen)
        clock.tick(fps)
        pygame.display.update()
        
        for i in range((position.height)*(position.width)):
            if brk[i] in allsprite:
                gamewin_judge = 0
                break
            
        if gamewin_judge == 1:
            return life,score_board.get_score(),True
        elif life >= 0:
            gamewin_judge = 1
        
    pygame.mixer.quit()
    pygame.quit()

def main():
    total_level = 10
    current_level = 1
    current_life = 3
    current_score = 0
    volume = 0.1
    windowWidth = 960
    windowHeight = windowWidth * 9 // 16
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight), pygame.SCALED)
    
    button = pygame.mixer.Sound(os.path.join("sounds", "button.wav"))
    button.set_volume(volume)
    soundplay = False

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    pygame.font.init()
    fontSize = windowWidth // 12
    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), fontSize)
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
    
    mainLoop = True
    while mainLoop:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*13//30 <= mouse[1] <= (windowHeight*13//30 + windowHeight//12):
                    game_judge = True
                    while game_judge:
                        
                        screen.fill((0,0,0))
                        screen.blit(font.render("Level %s"%current_level , True,  (255, 255, 255),(0, 0, 0)),(windowWidth//16*6,windowHeight//10*3)) 
                        pygame.display.update()  
                        pygame.time.wait(1000)
                        
                        current_life,current_score,game_judge = gameloop(current_level,current_life,current_score,volume)
                        
                        if game_judge and current_level < total_level:                            
                            current_level += 1
                        elif game_judge and current_level == total_level:
                            screen.fill((0,0,0))
                            screen.blit(font.render("Congratulation" , True,  (255, 255, 255),(0, 0, 0)),(windowWidth//16*5,windowHeight//10*3)) 
                            pygame.display.update()  
                            pygame.time.wait(2000)
                            current_level = 1
                            current_life = 3
                            current_score = 0
                            break
                        else:
                            screen.fill((0,0,0))
                            screen.blit(font.render("You lose" , True,  (255, 255, 255),(0, 0, 0)),(windowWidth//16*5,windowHeight//10*3)) 
                            pygame.display.update()  
                            pygame.time.wait(2000)
                            current_level = 1
                            current_life = 3
                            current_score = 0
                            break
                        
                elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*19//30 <= mouse[1] <= (windowHeight*19//30 + windowHeight//12):
                    pass
                elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*5//6 <= mouse[1] <= (windowHeight*5//6 + windowHeight//12):
                    mainLoop = False
        """
        change the background color of button
                                               """
        screen.blit(background, (0,0))
        if windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*13//30 <= mouse[1] <= (windowHeight*13//30 + windowHeight//12):
            pygame.draw.rect(screen,(0,0,0),(windowWidth*5//12,windowHeight*13//30,windowWidth//6, windowHeight//12))
            start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//5, windowHeight//10))
            screen.blit(start_button,(windowWidth//10*4,windowHeight*17//40))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*19//30 <= mouse[1] <= (windowHeight*19//30 + windowHeight//12):
            pygame.draw.rect(screen,(0,0,0),(windowWidth*5//12,windowHeight*19//30,windowWidth//6, windowHeight//12))
            option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//5, windowHeight//10))
            screen.blit(option_button,(windowWidth//10*4,windowHeight*5//8))
            if not soundplay:
                button.play()
                soundplay = True

        elif windowWidth*5//12 <= mouse[0] <= (windowWidth*5//12 + windowWidth//6) and windowHeight*5//6 <= mouse[1] <= (windowHeight*5//6 + windowHeight//12):
            pygame.draw.rect(screen,(0,0,0),(windowWidth*5//12,windowHeight*5//6,windowWidth//6, windowHeight//12))
            exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//5, windowHeight//10))
            screen.blit(exit_button,(windowWidth//10*4,windowHeight*33//40))
            if not soundplay:
                button.play()
                soundplay = True

        else:
            start_button = pygame.transform.smoothscale(start_button_pic, (windowWidth//6, windowHeight//12))
            screen.blit(start_button,(windowWidth*5//12,windowHeight*13//30))
            option_button = pygame.transform.smoothscale(option_button_pic, (windowWidth//6, windowHeight//12))
            screen.blit(option_button,(windowWidth*5//12,windowHeight*19//30))
            exit_button = pygame.transform.smoothscale(exit_button_pic, (windowWidth//6, windowHeight//12))
            screen.blit(exit_button,(windowWidth*5//12,windowHeight*5//6))
            soundplay = False
        
        pygame.display.update()  
    
    pygame.mixer.quit()
    pygame.quit()
if __name__ == "__main__":
    main()