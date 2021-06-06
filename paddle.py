import os , pygame

class paddle(pygame.sprite.Sprite):
   def  __init__(self,windowWidth,paddleWidth,paddleHeight):
       pygame.sprite.Sprite.__init__(self)
       self.windowWidth = windowWidth
       self.paddleWidth = paddleWidth
       self.paddleHeight = paddleHeight  
       self.image = pygame.image.load(os.path.join("images", "paddle1.png")).convert_alpha()     
       self.image = pygame.transform.smoothscale(self.image, (self.paddleWidth, self.paddleHeight))
       self.rect = self.image.get_rect()
       self.rect.x = int(windowWidth/2)
       self.rect.y = 500
       self.tempX = self.rect.x 

   def control(self,orient):
       if orient == 1 and (self.rect.x - 10)>=0:
           self.tempX -= 10          
       elif orient == 2 and (self.rect.x + self.paddleWidth + 10)<=self.windowWidth:
           self.tempX += 10
           
   def update(self):
       self.rect.x = self.tempX
       
       
   def getxy(self):
       return self.tempX,self.rect.y