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
       self.dir = 1

    def update(self):
       self.rect.x = self.tempx
       self.rect.y = self.tempy
       
       
    def ball_onpad(self,x,y):
        self.tempx = x - self.radius // 2
        self.tempy = y - self.radius 
        
    def move(self,speed):
        
        if self.dir==0:
            self.tempy -= speed
        elif self.dir==1:
            self.tempy -= speed//2
            self.tempx += speed//2
        elif self.dir==2:            
            self.tempx += speed
        elif self.dir==3:
            self.tempy += speed//2
            self.tempx += speed//2
        elif self.dir==4:
            self.tempy += speed
        elif self.dir==5:
            self.tempy += speed//2
            self.tempx -= speed//2
        elif self.dir==6:
            self.tempx -= speed
        elif self.dir==7:
            self.tempy -= speed//2
            self.tempx -= speed//2
      
    def collide(self,things):
        if things == "left":
            if self.dir == 7:
                self.dir = 1
            elif self.dir == 6:
                self.dir = 2
            elif self.dir == 5:
                self.dir = 3
        elif things == "right":
            if self.dir == 1:
                self.dir = 7
            elif self.dir == 2:
                self.dir = 6
            elif self.dir == 3:
                self.dir = 5
        elif things == "up":
            if self.dir == 1:
                self.dir = 3
            elif self.dir == 0:
                self.dir = 4
            elif self.dir == 7:
                self.dir = 5
        elif things == "down":
            if self.dir == 4:
                self.dir = 0
            elif self.dir == 3:
                self.dir = 1
            elif self.dir == 5:
                self.dir = 7
        
      
        
    
       
    