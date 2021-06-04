import position

class brick:
    
    def __init__( self, pg, screen, n):
        self.id = n   
        self.color = (255, 0, 0)
        self.pg = pg
        self.screen = screen
        self.i = int( (self.id) / 11 )
        self.j = int( (self.id) % 11 )
        
    def draw(self):
        
        if position.level1[self.i][self.j] == 1:
            self.pg.draw.rect(self.screen, self.color, (30*self.j, 10*self.i, 30, 10), 2)
        self.i += 1
        self.j += 1
        
    def __str__(self):
        return str(self.id) + '\n'