from setup import *


class Base:

    width, height = 45, 2
    color = (255,255,255)

    def __init__(self,y):
        self.position = pygame.Vector2(WINDOW_WIDTH / 2 - self.width /2,y)
        self.velocity = pygame.Vector2(0,0)


    def move(self, mousewheel_MovementInfo):
        self.velocity.x = mousewheel_MovementInfo / 4

    def baseWindow_EdgeCollision(self):
        baseLeft = self.position.x
        baseRight = self.position.x + self.width

        if baseLeft < 0:
            self.position.x = 0
        if baseRight > WINDOW_WIDTH:
            self.position.x = WINDOW_WIDTH - self.width
    
    def update(self, deltaTime):
        self.position += self.velocity * deltaTime
        self.baseWindow_EdgeCollision()
        self.velocity = pygame.Vector2(0,0)
    
    def draw(self, window):
        r = pygame.Rect(
            self.position.x, 
            self.position.y, 
            self.width, 
            self.height
        )
        
        pygame.draw.rect(
            window, 
            self.color,
            r
        )