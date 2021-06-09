import pygame 
class scoreboard(pygame.sprite.Sprite):
    def __init__(self, windowWidth, windowHeight):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.score = 0
        self.font = pygame.font.SysFont("None", 40)
        self.image = self.font.render("Score:%s   " % self.score, True,  (255, 255, 255),(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = windowWidth//2
        self.rect.y =windowHeight//50
    def update(self):
        self.image = self.font.render("Score:%s   " % self.score, True, (255, 255, 255), (0, 0, 0))
    
    
    def score_change(self,num):
        self.score += num
        
        
    def reset(self):
        self.score = 0
