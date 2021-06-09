import pygame 
import brick
import paddle
import position
import ball
import scoreboard
def main():
    ball_state = 'onpad'
    windowWidth = 1280
    windowHeight = windowWidth * 9 // 16
    
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

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
    
    ballx ,bally = pad.getxy()
    gameball = ball.ball(windowWidth, windowWidth, ballx, bally)
    allsprite.add(gameball)
    
    score_board = scoreboard.scoreboard(windowWidth, windowHeight)
    allsprite.add(score_board)
    
    clock = pygame.time.Clock()
    fps = 60
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    pad.left = False
                elif event.key == pygame.K_RIGHT or event.key == ord('d') :
                    pad.right = False
        
        pad.move(speed)

        if ball_state == 'onpad':
            x , y = pad.getxy()
            x +=  pad.paddleWidth // 2
            gameball.ball_onpad(x, y)
        
        screen.blit(background, (0, 0))
        
        for sprite in allsprite:
            sprite.update()
        allsprite.draw(screen)
        clock.tick(fps)
        pygame.display.update()
        

    pygame.quit()



if __name__ == "__main__":
    main()