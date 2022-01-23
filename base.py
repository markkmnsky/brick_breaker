### BASE.PY = encompasses everything to do with the base,
# mainly the movement of the base when the scroll wheel is moved
# the collision detection of when the base hits the edge of the screen
# and the update and draw methods 

# setup import
from setup import *


class Base:

    # defining static var
    width, height = 100, 2
    color = (255,255,255)
    speedFactor = 3

    def __init__(self,y): # initializing position and velocity, dynamic variables
        self.position = pygame.Vector2(WINDOW_WIDTH / 2 - self.width /2,y)
        self.velocity = pygame.Vector2(0,0)


    def move(self, mousewheel_MovementInfo): # if the mouse wheel is moved, this changes the velocity in the respective direction
        self.velocity.x = mousewheel_MovementInfo / self.speedFactor

    def baseWindow_EdgeCollision(self): # checks to see if the base will hit the side of the window, and stops it from moving if it will
        baseLeft = self.position.x
        baseRight = self.position.x + self.width

        if baseLeft < 0: # if left side
            self.position.x = 0
        if baseRight > WINDOW_WIDTH: # if right side
            self.position.x = WINDOW_WIDTH - self.width
    
    def update(self, deltaTime): # update
        self.position += self.velocity * deltaTime
        self.baseWindow_EdgeCollision()
        self.velocity = pygame.Vector2(0,0)
    
    def draw(self, window): # draw function, just like all others
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