from setup import *

class Brick:
    width = 64
    height = 32
    color = (255, 255, 255)

    def __init__(self, x, y):
        self.position = pygame.Vector2(x,y)

    def draw(self, screen):
        r = pygame.Rect(
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )
        pygame.draw.rect(screen, self.color, r)

    def __repr__(self) -> str:
        return f"Brick<{self.position.x}, {self.position.y}>"


    