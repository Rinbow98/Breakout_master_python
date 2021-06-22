import os, pygame
import position

class brick(pygame.sprite.Sprite):
    
    def __init__( self, n, windowWidth, windowHeight , bonus ):
        pygame.sprite.Sprite.__init__(self)
        self.id = n
        self.stage = 0
        self.i = int( (self.id) / position.width )
        self.j = int( (self.id) % position.width )
        self.brickWidth = windowWidth//position.width
        self.brickHeight = windowHeight//position.width
        self.image_pic = pygame.image.load(os.path.join("images", "greenBrick1.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image_pic, (self.brickWidth, self.brickHeight))
        self.rect = self.image.get_rect()
        self.rect.x = self.j*self.brickWidth
        self.rect.y = (self.i+2)*self.brickHeight
        self.point = 10
        self.bonus = bonus
        self.state = 'stationary'
        self.tempy = self.rect.y
        self.bonusWidth = windowWidth//21
        self.bonusHeight = windowHeight // 15
        self.hit_tick = pygame.time.get_ticks()

        
    def __str__(self):
        return str(self.id)

    def reset(self):
        pass

    def change(self, windowWidth, windowHeight):
        self.brickWidth = windowWidth//position.width
        self.brickHeight = windowHeight//position.width
        self.image = pygame.transform.smoothscale(self.image_pic, (self.brickWidth, self.brickHeight))
        self.rect = self.image.get_rect()
        self.rect.x = self.j*self.brickWidth
        self.rect.y = (self.i+2)*self.brickHeight
    
    def bonus_judge(self):
        if self.bonus == 0:
            pass
        elif self.bonus == 1:
             self.image_pic = pygame.image.load(os.path.join("images", "bonusPenetrate.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.bonusWidth, self.bonusHeight))
             self.state = 'dropping'
        elif self.bonus == 2:
             self.image_pic = pygame.image.load(os.path.join("images", "bonusSticky.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.bonusWidth, self.bonusHeight))
             self.state = 'dropping'
        elif self.bonus == 3:
             self.image_pic = pygame.image.load(os.path.join("images", "bonusWide.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.bonusWidth, self.bonusHeight))
             self.state = 'dropping'
        elif self.bonus == 4:
             self.image_pic = pygame.image.load(os.path.join("images", "bonusNarrow.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.bonusWidth, self.bonusHeight))
             self.state = 'dropping'
        elif self.bonus == 5:
             self.image_pic = pygame.image.load(os.path.join("images", "bonusAddball.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.bonusWidth, self.bonusHeight))
             self.state = 'dropping'
             
    def move(self):
        self.tempy += 5
              
    def update(self):
        self.rect.y = self.tempy
    
    def set_stage(self,stage):
        self.stage = stage
        if self.stage == 3:
             self.image_pic = pygame.image.load(os.path.join("images", "greenBrick1.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.brickWidth, self.brickHeight))
        elif self.stage == 2:
             self.image_pic = pygame.image.load(os.path.join("images", "yellowBrick1.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.brickWidth, self.brickHeight))
        elif self.stage == 1:
             self.image_pic = pygame.image.load(os.path.join("images", "redBrick1.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.brickWidth, self.brickHeight))
    
    def change_stage(self):
        self.stage -= 1
        self.hit_tick = pygame.time.get_ticks()
        if self.stage == 2:
             self.image_pic = pygame.image.load(os.path.join("images", "yellowBrick1.png")).convert_alpha()
             self.image = pygame.transform.smoothscale(self.image_pic, (self.brickWidth, self.brickHeight))
        else:
            self.image_pic = pygame.image.load(os.path.join("images", "redBrick1.png")).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image_pic, (self.brickWidth, self.brickHeight))
