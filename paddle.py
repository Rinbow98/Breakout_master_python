import os, pygame

class paddle(pygame.sprite.Sprite):
    
    def  __init__(self, windowWidth, windowHeight, speed):
        pygame.sprite.Sprite.__init__(self)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.paddleWidth = self.windowWidth // 6
        self.paddleHeight = self.windowWidth // 96
        self.image_pic = pygame.image.load(os.path.join("images", "paddle1.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))
        self.rect = self.image.get_rect()
        self.rect.x = self.windowWidth // 2
        self.rect.y = self.windowHeight // 12 * 11
        self.tempX = self.rect.x
        self.right = False
        self.left = False
        self.speed = speed
        self.max_paddleWidth = self.windowWidth // 4
        self.min_paddleWidth = self.windowWidth // 8
        

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
        self.max_paddleWidth = windowWidth // 3
        self.min_paddleWidth = windowWidth // 9
        
    def longer_paddle(self):
        if self.paddleWidth + self.paddleWidth*2//10 <= self.max_paddleWidth:
            self.tempX -= self.paddleWidth//10
            self.paddleWidth += self.paddleWidth*2//10
            if self.tempX <= 0:
                self.tempX = 0
            self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))
            
    def shorter_paddle(self):
        if self.paddleWidth - self.paddleWidth//6 >= self.min_paddleWidth:
            self.tempX += self.paddleWidth//12
            self.paddleWidth -= self.paddleWidth//6
            if self.tempX >= self.windowWidth - self.paddleWidth:
                self.tempX = self.windowWidth - self.paddleWidth
            self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))

    def sticky(self, bonus):
        if bonus:
            self.image_pic = pygame.image.load(os.path.join("images", "paddleSticky1.png")).convert_alpha()
        else:
            self.image_pic = pygame.image.load(os.path.join("images", "paddle1.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))
        self.rect = self.image.get_rect()
        self.rect.x = self.tempX
        self.rect.y = self.windowHeight // 12 * 11

    def reset(self):
        self.paddleWidth = self.windowWidth // 6
        self.image_pic = pygame.image.load(os.path.join("images", "paddle1.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image_pic, (self.paddleWidth, self.paddleHeight))
        self.rect = self.image.get_rect()
        self.rect.x = self.tempX
        self.rect.y = self.windowHeight // 12 * 11