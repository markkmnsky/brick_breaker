from setup import *
from ball import Ball
from brick import Brick
from base import Base



class Fundamental:
    bricks_rows = 7
    bricks_columns = 5
    
    
    def __init__(self):
        self.ball = Ball(300,300)
        self.base = Base(WINDOW_HEIGHT - 55)
        self.bricks = []

        for row in range(self.bricks_rows):
            self.bricks.append([])
            for column in range(self.bricks_columns):
                self.bricks[row].append(Brick(100 * column, 50 * row))



    def update(self, deltaTime):


        mousewheel_MovementInfo = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXITEVENT
            elif event.type == pygame.MOUSEWHEEL:
                mousewheel_MovementInfo = event.y

                
        self.base.move(mousewheel_MovementInfo)
        self.base.update(deltaTime)
        self.ball.update(deltaTime, self.base, self.bricks)
    
    def draw(self, window):

        self.ball.draw(window)
        self.base.draw(window)
        for row in self.bricks:
            for brick in row:
                brick.draw(window)
