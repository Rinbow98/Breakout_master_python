import os, pygame

class paddle(pygame.sprite.Sprite):
    def  __init__(self, windowWidth, windowHeight, speed):
        pygame.sprite.Sprite.__init__(self)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.paddleWidth = windowWidth // 6
        self.paddleHeight = windowWidth // 96
        self.image_pic = pygame.image.load(os.path.join("images", "paddle1.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))
        self.rect = self.image.get_rect()
        self.rect.x = windowWidth // 2
        self.rect.y = windowHeight // 12 * 11
        self.tempX = self.rect.x
        self.right = False
        self.left = False
        self.speed = speed
        self.max_paddleWidth = windowWidth // 4
        self.min_paddleWidth = windowWidth // 8
        
    def move(self):
        if self.left and self.rect.x - self.speed >= 0:
            self.tempX -= self.speed
        elif self.right and self.rect.x + self.paddleWidth + self.speed <= self.windowWidth:
            self.tempX += self.speed
           
           
    def update(self):
        self.rect.x = self.tempX
       
       
    def getxy(self):
       return self.tempX, self.rect.y

    def change(self, windowWidth, windowHeight):
        self.paddleWidth = windowWidth // 6
        self.paddleHeight = windowWidth // 96
        self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.x * windowWidth // self.windowWidth
        self.rect.y = windowHeight // 12 * 11
        self.tempX = self.tempX * windowWidth // self.windowWidth
        self.speed = self.speed * windowWidth // self.windowWidth
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.max_paddleWidth = windowWidth // 4
        self.min_paddleWidth = windowWidth // 8
        
    def longer_paddle(self):
        if self.paddleWidth + self.paddleWidth*2//10 <= self.max_paddleWidth:
            self.paddleWidth += self.paddleWidth*2//10
            self.image_pic = pygame.image.load(os.path.join("images", "paddle1.png")).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))
            
    def shorter_paddle(self):
        if self.paddleWidth - self.paddleWidth*2//10 >= self.min_paddleWidth:
            self.paddleWidth -= self.paddleWidth*2//10
            self.image_pic = pygame.image.load(os.path.join("images", "paddle1.png")).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))