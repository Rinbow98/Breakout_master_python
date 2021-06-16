import os, pygame
import position

class brick(pygame.sprite.Sprite):
    
    def __init__( self, n, windowWidth, windowHeight):
        pygame.sprite.Sprite.__init__(self)
        self.id = n
        self.i = int( (self.id) / position.width )
        self.j = int( (self.id) % position.width )
        self.brickWidth = windowWidth//position.width
        self.brickHeight = windowHeight//position.width
        self.image_pic = pygame.image.load(os.path.join("images", "redBrick1.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image_pic, (self.brickWidth, self.brickHeight))
        self.rect = self.image.get_rect()
        self.rect.x = self.j*self.brickWidth
        self.rect.y = (self.i+2)*self.brickHeight
        self.point = 10
         
        
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