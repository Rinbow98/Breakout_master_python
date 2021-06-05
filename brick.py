import position, os

class brick:
    
    def __init__( self, pg, screen, n, windowWidth, windowHeight):
        self.id = n   
        self.pg = pg
        self.screen = screen
        self.i = int( (self.id) / position.width )
        self.j = int( (self.id) % position.width )
        self.imagex = windowWidth//position.width
        self.imagey = windowHeight//position.width
        self.image = self.pg.image.load(os.path.join("images", "redBrick1.png")).convert_alpha()
        self.image = pg.transform.smoothscale(self.image, (self.imagex, self.imagey))

    def draw(self):

        if position.level[self.i][self.j] == 1:
          self.screen.blit(self.image, (self.j*self.imagex, (self.i+3)*self.imagey))
         
        
    def __str__(self):
        return str(self.id) + '\n'