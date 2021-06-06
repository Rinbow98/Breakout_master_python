import pygame 
import brick
import paddle
import position
import ball

def main():
    ball_state = 'onpad'
    windowWidth = 720
    windowHeight = 540
    paddleWidth = 100
    paddleHeight = 15
    
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
            
    pad = paddle.paddle(windowWidth,paddleWidth,paddleHeight)
    allsprite.add(pad)
    
    ballx ,bally = pad.getxy()
    ball1 = ball.ball(windowWidth,windowHeight,ballx,bally)
    allsprite.add(ball1)
    
    
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    pad.control(1)   
                elif event.key == pygame.K_RIGHT or event.key == ord('d') :
                    pad.control(2)
            if ball_state == 'onpad':
                x , y = pad.getxy()
                x +=  int(paddleWidth / 2)
                ball1.ball_onpad(x,y)
            
        
        screen.blit(background,(0,0))
        
        for sprite in allsprite:
            sprite.update()
        allsprite.draw(screen)
        pygame.display.update()
        
if __name__ == "__main__":
    main()