import os, pygame
import position

class brick(pygame.sprite.Sprite):
    
    def __init__( self, n, windowWidth, windowHeight):
        pygame.sprite.Sprite.__init__(self)
        self.id = n
        self.i = int( (self.id) / position.width )
        self.j = int( (self.id) % position.width )
        self.imagex = windowWidth//position.width
        self.imagey = windowHeight//position.width
        self.image = pygame.image.load(os.path.join("images", "redBrick1.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (self.imagex, self.imagey))
        self.rect = self.image.get_rect()
        self.rect.x = self.j*self.imagex
        self.rect.y = (self.i+3)*self.imagey
    
         
        
    def __str__(self):
        return str(self.id) + '\n'