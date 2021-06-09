import os, pygame

class paddle(pygame.sprite.Sprite):
   def  __init__(self, windowWidth, windowHeight):
       pygame.sprite.Sprite.__init__(self)
       self.windowWidth = windowWidth
       self.paddleWidth = windowWidth // 6
       self.paddleHeight = windowWidth // 48
       self.image = pygame.image.load(os.path.join("images", "paddle1.png")).convert_alpha()
       self.image = pygame.transform.smoothscale(self.image, (self.paddleWidth, self.paddleHeight))
       self.rect = self.image.get_rect()
       self.rect.x = windowWidth // 2
       self.rect.y = windowHeight // 12 * 11
       self.tempX = self.rect.x 
       self.right = False
       self.left = False

   def move(self, speed):
       if self.left and self.rect.x - speed >= 0:
           self.tempX -= speed
       elif self.right and self.rect.x + self.paddleWidth + speed <= self.windowWidth:
           self.tempX += speed
           
           
   def update(self):
       self.rect.x = self.tempX
       
       
   def getxy(self):
       return self.tempX,self.rect.y