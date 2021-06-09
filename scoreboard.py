import os, pygame

class scoreboard(pygame.sprite.Sprite):
    def __init__(self, windowWidth, windowHeight):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.windowWidth = windowWidth
        self.score = 0
        self.fontSize = windowWidth // 32
        self.font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), self.fontSize)
        self.image = self.font.render("Score:%s" % self.score, True,  (255, 255, 255),(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = (windowWidth - ( 6+len(str(self.score)) )*self.fontSize//2) // 2
        self.rect.y = windowHeight // 50


    def update(self):
        self.rect.x = (self.windowWidth - ( 6+len(str(self.score)) )*self.fontSize//2) // 2
        self.image = self.font.render("Score:%s" % self.score, True, (255, 255, 255), (0, 0, 0))
    
    
    def add(self,num):
        self.score += num
        
        
    def reset(self):
        self.score = 0
