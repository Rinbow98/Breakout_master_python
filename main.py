import pygame, math
import ball, brick, paddle, position, scoreboard

def main():

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
        if position.level[k][j] == 1:
            allsprite.add(brk[i])
            
    pad = paddle.paddle(windowWidth, windowHeight, speed)
    allsprite.add(pad)

    gameball = ball.ball(windowWidth, windowWidth, pad.tempX, pad.rect.y, speed)
    allsprite.add(gameball)
    
    score_board = scoreboard.scoreboard(windowWidth, windowHeight)
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
                mainLoop = False
                

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
        

    pygame.quit()



if __name__ == "__main__":
    main()