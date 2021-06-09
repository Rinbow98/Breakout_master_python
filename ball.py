import os, pygame

class ball(pygame.sprite.Sprite):
    def  __init__(self,windowWidth,windowHeight,x,y):
       pygame.sprite.Sprite.__init__(self)
       self.windowWidth = windowWidth
       self.windowHight = windowHeight
       self.radius = windowWidth // 36
       self.image = pygame.image.load(os.path.join("images", "ball2.png")).convert_alpha()     
       self.image = pygame.transform.smoothscale(self.image, (self.radius, self.radius))
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y - self.radius
       self.state = 'onpad'
       self.tempx = 0
       self.tempy = 0

       
    def update(self):
       self.rect.x = self.tempx
       self.rect.y = self.tempy
       
       
    def ball_onpad(self,x,y):
        self.tempx = x - self.radius // 2
        self.tempy = y - self.radius
        
    