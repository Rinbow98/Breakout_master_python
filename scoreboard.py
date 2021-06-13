import os, pygame

class scoreboard(pygame.sprite.Sprite):
    def __init__(self, windowWidth, windowHeight,life,score):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.windowWidth = windowWidth
        self.score = score
        self.life = life
        self.fontSize = windowWidth // 32
        self.font = pygame.font.Font(os.path.join("fonts", "comicsansms.ttf"), self.fontSize)
        self.image = self.font.render(" Score:%s                      Life:%s" % (self.score, self.life), True,  (255, 255, 255),(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = (windowWidth - ( 6+len(str(self.score)+str(self.life)) )*self.fontSize//2) // 2
        self.rect.y = windowHeight // 50


    def update(self):
        self.rect.x = (self.windowWidth - ( 6+len(str(self.score)+str(self.life)) )*self.fontSize//2) // 2
        self.image = self.font.render("Score:%s                        Life:%s" %( self.score, self.life), True, (255, 255, 255), (0, 0, 0))
    
    
    def add(self,num):
        self.score += num
        
        
    def reset(self):
        self.score = 0
        
    def losslife(self):
        self.life -= 1
    
    def get_score(self):
        return self.score