import pygame, math , os
import ball, brick, paddle, position, scoreboard

def gameloop(lev,lif,sco):
    level = lev
    life = lif
    score = sco
    
    gamewin_judge = 1
    windowWidth = 960
    windowHeight = windowWidth * 9 // 16
    
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight), pygame.SCALED)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    pygame.draw.line(background, (255, 255, 255), (0, windowHeight//10), (windowWidth, windowHeight//10), 1)
    

    clock = pygame.time.Clock()
    fps = 60
    speed = windowWidth // fps // 2
    allsprite = pygame.sprite.Group()
    
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
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    pad.left = False
                elif event.key == pygame.K_RIGHT or event.key == ord('d') :
                    pad.right = False
                    
        if gameball.state == 'moving':
            gameball.move(speed)
            x = gameball.rect.x+gameball.dx*2-pad.rect.x-pad.paddleWidth/2
            if gameball.rect.x+gameball.dx*2 <= 0:
                gameball.collide("x")

            elif gameball.rect.x+gameball.radius+gameball.dx*2 >= windowWidth:
                gameball.collide("x")

            elif gameball.rect.y+gameball.dy*2 <= windowHeight // 10:
                gameball.collide("y")

            elif gameball.rect.y+gameball.radius+gameball.dy*2 >= pad.rect.y and gameball.rect.y <= pad.rect.y+pad.paddleHeight and abs(x) <= pad.paddleWidth/2:
                if abs(x) > pad.paddleWidth/10:
                    angle = x/pad.paddleWidth*math.pi/3+math.pi/3
                    if gameball.angle > angle:
                        gameball.angle = math.pi/6*5-(math.pi/6*5-gameball.angle)*(angle-math.pi/6)/(math.pi/6*5-angle)
                    elif gameball.angle < angle:
                        gameball.angle = (gameball.angle-math.pi/6)*(math.pi/6*5-angle)/(angle-math.pi/6)+math.pi/6
                gameball.collide("y")
        
            elif gameball.rect.y+gameball.radius+gameball.dy*2 >= windowHeight:
                if life-1 > 0:
                    life -= 1
                    score_board.losslife()
                    gameball.state = 'onpad'
                else:
                    return life,score_board.get_score(),False
            for i in range((position.height)*(position.width)):
                if  allsprite.has(brk[i]) and gameball.rect.y+gameball.dy*2 <= brk[i].rect.y+brk[i].brickHeight and gameball.rect.y+gameball.radius+gameball.dy*2 >= brk[i].rect.y and gameball.rect.x+gameball.dx*2 <= brk[i].rect.x+brk[i].brickWidth and gameball.rect.x+gameball.radius+gameball.dx*2 >= brk[i].rect.x:
                    score_board.add(brk[i].point)
                    allsprite.remove(brk[i])
                    
                    if gameball.rect.x > brk[i].rect.x+brk[i].brickWidth or gameball.rect.x+gameball.radius < brk[i].rect.x:
                        gameball.collide("x")
                    else:
                        gameball.collide("y")
            
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
        
            

    pygame.quit()

def main():
    total_level = 10
    current_level = 1
    current_life = 3
    current_score = 0
    windowWidth = 960
    windowHeight = windowWidth * 9 // 16
    
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight), pygame.SCALED)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    pygame.font.init()
    fontSize = windowWidth // 12
    font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), fontSize)
    breakout = font.render("Breakout" , True,  (255, 255, 255),(0, 0, 0))
    background.blit(breakout,(windowWidth//15*5,windowHeight//12))
    
    start_button = pygame.image.load(os.path.join("images", "start.png")).convert_alpha()     
    start_button = pygame.transform.smoothscale(start_button, (windowWidth//6, windowHeight//12))
    background.blit(start_button,(windowWidth//16*7,windowHeight//10*4))
    
    option_button = pygame.image.load(os.path.join("images", "option.png")).convert_alpha()     
    option_button = pygame.transform.smoothscale(option_button, (windowWidth//6, windowHeight//12))
    background.blit(option_button,(windowWidth//16*7,windowHeight//10*6))
    
    exit_button = pygame.image.load(os.path.join("images", "exit.png")).convert_alpha()     
    exit_button = pygame.transform.smoothscale(exit_button, (windowWidth//6, windowHeight//12))
    background.blit(exit_button,(windowWidth//16*7,windowHeight//10*8))
   
    
    screen.blit(background, (0,0))
    
    mainLoop = True
    while mainLoop:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if windowWidth//16*7 <= mouse[0] <= (windowWidth//16*7 + windowWidth//6) and windowHeight//10*4 <= mouse[1] <= (windowHeight//10*4 + windowHeight//12):
                    game_judge = True
                    while game_judge:
                        
                        screen.fill((0,0,0))
                        screen.blit(font.render("Level %s"%current_level , True,  (255, 255, 255),(0, 0, 0)),(windowWidth//16*6,windowHeight//10*3)) 
                        pygame.display.update()  
                        pygame.time.wait(1000)
                        
                        current_life,current_score,game_judge = gameloop(current_level,current_life,current_score)
                        
                        if game_judge and current_level < total_level:                            
                            current_level += 1
                        elif game_judge and current_level == total_level:
                            screen.fill((0,0,0))
                            screen.blit(font.render("You win" , True,  (255, 255, 255),(0, 0, 0)),(windowWidth//16*5,windowHeight//10*3)) 
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
                        
                elif windowWidth//16*7 <= mouse[0] <= (windowWidth//16*7 + windowWidth//6) and windowHeight//10*6 <= mouse[1] <= (windowHeight//10*6 + windowHeight//12):
                    pass
                elif windowWidth//16*7 <= mouse[0] <= (windowWidth//16*7 + windowWidth//6) and windowHeight//10*8 <= mouse[1] <= (windowHeight//10*8 + windowHeight//12):
                    mainLoop = False
        """
        change the background color of button
                                               """
        screen.blit(background, (0,0))
        if windowWidth//16*7 <= mouse[0] <= (windowWidth//16*7 + windowWidth//6) and windowHeight//10*4 <= mouse[1] <= (windowHeight//10*4 + windowHeight//12):
             pygame.draw.rect(screen,(0,255,0),(windowWidth//16*7,windowHeight//10*4,windowWidth//6, windowHeight//12))
        else:
            pygame.draw.rect(screen,(0,0,0),(windowWidth//16*7,windowHeight//10*4,windowWidth//6, windowHeight//12))
        screen.blit(start_button,(windowWidth//16*7,windowHeight//10*4))
        
        if windowWidth//16*7 <= mouse[0] <= (windowWidth//16*7 + windowWidth//6) and windowHeight//10*6 <= mouse[1] <= (windowHeight//10*6 + windowHeight//12):
             pygame.draw.rect(screen,(0,255,0),(windowWidth//16*7,windowHeight//10*6,windowWidth//6, windowHeight//12))
        else:
            pygame.draw.rect(screen,(0,0,0),(windowWidth//16*7,windowHeight//10*6,windowWidth//6, windowHeight//12))
        screen.blit(option_button,(windowWidth//16*7,windowHeight//10*6))
        
        if windowWidth//16*7 <= mouse[0] <= (windowWidth//16*7 + windowWidth//6) and windowHeight//10*8 <= mouse[1] <= (windowHeight//10*8 + windowHeight//12):
             pygame.draw.rect(screen,(0,255,0),(windowWidth//16*7,windowHeight//10*8,windowWidth//6, windowHeight//12))
        else:
            pygame.draw.rect(screen,(0,0,0),(windowWidth//16*7,windowHeight//10*8,windowWidth//6, windowHeight//12))
        screen.blit(exit_button,(windowWidth//16*7,windowHeight//10*8))
        
        pygame.display.update()  
        
    pygame.quit()
if __name__ == "__main__":
    main()