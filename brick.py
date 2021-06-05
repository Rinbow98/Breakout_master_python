import position

class brick:
    
    def __init__( self, pg, screen, n):
        self.id = n   
        self.pg = pg
        self.screen = screen
        self.i = int( (self.id) / position.width )
        self.j = int( (self.id) % position.width)
        self.windowWidth = 1280
        self.windowHeight = 720
        self.brk_image = self.pg.image.load("C:\\Users\\david\\Desktop\\python\\期末專題\\GitHub\\Breakout_master_python\\images\\redBrick5.png")
    def draw(self):       
        self.brk_image.convert()        
        if position.level[self.i][self.j] == 1:
          self.screen.blit(self.brk_image, (self.j*64,self.i*36+200))
         
        
    def __str__(self):
        return str(self.id) + '\n'