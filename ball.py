import os, pygame, random, math

class ball(pygame.sprite.Sprite):
    def  __init__(self, windowWidth, windowHeight, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.windowWidth = windowWidth
        self.windowHight = windowHeight
        self.radius = windowWidth // 72
        self.image = pygame.image.load(os.path.join("images", "ball1.png")).convert_alpha()     
        self.image = pygame.transform.smoothscale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.radius
        self.state = 'onpad'
        self.tempx = 0
        self.tempy = 0
        self.speed = speed
        self.angle = random.random()*math.pi/3*2 + math.pi/6*7
        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)

    def update(self):
        self.rect.x = self.tempx
        self.rect.y = self.tempy
       
    def onpad(self,x,y):
        self.tempx = x - self.radius // 2
        self.tempy = y - self.radius - 1
        
    def move(self,speed):
        self.tempx += self.dx
        self.tempy += self.dy
    
    def collide(self,dir):
        if dir == "x":
            self.angle = math.pi-self.angle
        elif dir == "y":
            self.angle = -self.angle
        self.angle %= math.pi*2
        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)
        
      
        
    
       
    