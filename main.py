import pygame 
import ball, brick, paddle, position, scoreboard

def main():
    ball_state = 'onpad'
    windowWidth = 1280
    windowHeight = windowWidth * 9 // 16
    
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    pygame.draw.line(background, (255, 255, 255), (0, windowHeight//10), (windowWidth, windowHeight//10), 1)

    allsprite = pygame.sprite.Group()
    
    brk = [None]*1000
    for i in range((position.height)*(position.width)):
        brk[i] = brick.brick( i, windowWidth, windowHeight)
        k = int( (i) / position.width )
        j = int( (i) % position.width )
        if position.level[k][j] == 1:
            allsprite.add(brk[i])
            
    pad = paddle.paddle(windowWidth, windowHeight)
    allsprite.add(pad)
    

    gameball = ball.ball(windowWidth, windowWidth, pad.tempX, pad.rect.y)
    allsprite.add(gameball)
    
    score_board = scoreboard.scoreboard(windowWidth, windowHeight)
    allsprite.add(score_board)
    
    clock = pygame.time.Clock()
    fps = 30
    speed = windowWidth // fps // 2
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
                    if ball_state == 'onpad':
                        ball_state = 'moving'
                    
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    pad.left = False
                elif event.key == pygame.K_RIGHT or event.key == ord('d') :
                    pad.right = False
                    
        if ball_state == 'moving':            
            gameball.move(speed)
            if gameball.rect.x <= 0 :           
                gameball.collide("left")
                
            elif gameball.rect.x >= windowWidth - 2*gameball.radius :
                gameball.collide("right")
                
            elif gameball.rect.y <= windowHeight // 10:
                gameball.collide("up")           
        
            elif gameball.rect.y >= windowHeight - 2*gameball.radius:
                mainLoop = False
                
            elif  gameball.rect.colliderect( pad ):
                gameball.collide("down")

            for i in range((position.height)*(position.width)):
                if  gameball.rect.colliderect( brk[i].rect ) and allsprite.has(brk[i]):
                    score_board.add(brk[i].point)
                    allsprite.remove(brk[i])
                    if gameball.rect.y >= brk[i].rect.y:
                        gameball.collide("up")
                    else:
                        gameball.collide("down")

                 #mainLoop = False
        pad.move(speed)

        if ball_state == 'onpad':
            x , y = pad.getxy()
            x +=  pad.paddleWidth // 2
            gameball.ball_onpad(x, y)
        elif ball_state == 'moving':
            gameball.move(speed//2)

        screen.blit(background, (0, 0))
        
        for sprite in allsprite:
            sprite.update()
        allsprite.draw(screen)
        clock.tick(fps)
        pygame.display.update()
        

    pygame.quit()



if __name__ == "__main__":
    main()