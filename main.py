import pygame as pg
import brick
import position

def main():

    windowWidth = 720
    windowHeight = 540

    pg.init()
    screen = pg.display.set_mode((windowWidth, windowHeight))
    screen.fill((0, 0, 0))
    brk = [None]*1000
    for i in range((position.height)*(position.width)):
        brk[i] = brick.brick(pg, screen, i, windowWidth, windowHeight)
        brk[i].draw()

        

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    
        #surface.blit(image, (25, 25))
        pg.display.update()


if __name__ == "__main__":
    main()