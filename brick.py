### BRICK.PY = encompasses everything to do with the base, 
# mainly the variables surrounding size and color,
# and the draw method + __repr__ functionality which simplifies code later on#

#setup import
from setup import *

class Brick:
    # defining static var
    width = 48
    height = 24
    color = (255, 255, 255)

    def __init__(self, x, y):
        # defining dynamic var
        self.position = pygame.Vector2(x,y)

    def draw(self, screen): # draws
        r = pygame.Rect(
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )
        pygame.draw.rect(screen, self.color, r)

    def __repr__(self) -> str:
        return f"Brick<{self.position.x}, {self.position.y}>"


    