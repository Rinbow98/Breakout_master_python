# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:48:05 2021

@author: david
"""
import pygame as pg
import brick
import position
pg.init()
screen = pg.display.set_mode((400,600))
screen.fill((255,255,255))
brk = [None]*100                          
for i in range((position.length-1)*(position.width-1)):
    #brk[i] = i
   brk[i] = brick.brick(pg,screen,i)
   brk[i].draw()










  




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    #surface.blit(image, (25, 25))
    pg.display.update()                                  
