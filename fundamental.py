###### © Mark Kaminsky 2022. All rights reserved.

### FUNDAMENTAL.PY = the main game logic and scene, 
# holds the information of the brick placement in the levels
# initializes and controls the different parts of the game (brick, base, ball)
# does all of the main game logic and calls for all of the parts to be updated,
# and calls for GameOverInit to be done, to save and read the final scores#

# various imports are used to gather data from different parts of the game for calculations, and to call their respective update and draw methods
from setup import *
from ball import Ball
from brick import Brick
from base import Base
from highscore_manager import GameOverInit

#defining static var of how many rows and columns there are in the game, used to help draw the bricks on the screen
LEVEL_ROWS = 9
LEVEL_COLUMNS = 8

# levels
LEVEL_1 = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,0,0,1,0,0],
    [0,1,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0],
    [0,0,1,0,0,1,0,0]
]
LEVEL_2 = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0],
    [0,1,1,1,1,1,1,0],
    [1,1,1,0,0,1,1,1],
    [0,1,1,1,1,1,1,0],
    [0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]
LEVEL_3 = [
    [1,1,1,0,0,1,1,1],
    [1,1,1,0,0,1,1,1],
    [0,0,0,0,0,0,0,0],
    [1,1,1,0,0,1,1,1],
    [1,1,1,0,0,1,1,1],
    [0,0,0,0,0,0,0,0],
    [1,1,1,0,0,1,1,1],
    [1,1,1,0,0,1,1,1],
    [0,0,0,0,0,0,0,0]
]
LEVEL_4 = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,0,0,1,1,1],
    [1,1,0,0,0,0,1,1],
    [1,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0]
]
LEVEL_5 = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0],
    [1,1,1,0,0,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,0,0,1,1,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]


LEVELS = [LEVEL_1,LEVEL_2,LEVEL_3,LEVEL_4,LEVEL_5,]

class Fundamental:

    def __init__(self):
        
        # defining dynamic vars
        self.ball = Ball()
        self.base = Base(WINDOW_HEIGHT - 55)
        self.gameoverinit = GameOverInit()
        self.bricks = []

        self.level = 0
        self.generateLevel() # calls the generate function level, which generates the coordinates of the bricks to place them on the screen in a level


    def generateLevel(self):

        
        spacingFactor = 1.2 # spacing factor of the bricks

        # level width and height in pixels, used for calculations
        levelWidth_pxl = Brick.width * spacingFactor * (LEVEL_COLUMNS - 1) + Brick.width
        levelHeight_pxl = Brick.height * spacingFactor * (LEVEL_ROWS - 1) + Brick.height

        # offset
        offsetX = WINDOW_WIDTH / 2 - levelWidth_pxl / 2
        offsetY = WINDOW_HEIGHT / 2 - levelHeight_pxl / 2 - 150
        
        # appends a brick to the self.bricks level if it's in the level
        for row in range(LEVEL_ROWS):
            for column in range(LEVEL_COLUMNS):
                if LEVELS[self.level][row][column] == 1:
                    self.bricks.append(Brick(offsetX + Brick.width * spacingFactor * column, offsetY + Brick.height * spacingFactor * row))



        



    def update(self, deltaTime): # update function for game logic


        mousewheel_MovementInfo = 0 # sets and resets the scroll wheel movement info

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXITEVENT# returns exit event if closed
            elif event.type == pygame.MOUSEWHEEL:
                mousewheel_MovementInfo = event.y # gathers scroll input into mousewheel_MovementInfo

                
        self.base.move(mousewheel_MovementInfo) # moves base with the scroll wheel info
        self.base.update(deltaTime) # calls update func of base
        
        ballStatus = self.ball.update(deltaTime, self.base, self.bricks) # calls for ball to be updated, and gathers the returned status (if returned)

        if ballStatus == DEADEVENT: # if the ball hits the floor
            if self.ball.lives <= 0: # if the game is out of lives
                self.gameoverinit.update_NewScore(self.ball.scoreCounter) # updates high_scores.json with the score
                return GAMEOVER # returns gameover to the main file




        if len(self.bricks) == 0: # if all of the bricks are done
            self.level += 1 # next level
            self.ball.reset() # resets ball pos

            if self.level == len(LEVELS): # if all levels are complete
                return WINNINGSTATUS # returns winning status
            self.generateLevel() # otherwise, generate new level


    def printCounter(self, window): # prints score counter on bottom right of screen
        text_font = FONT_SMALL
        text_color = (255,255,255)
        posX = WINDOW_WIDTH - 20
        posY = WINDOW_HEIGHT - 25

        textSurface = text_font.render(str(self.ball.scoreCounter), True, text_color, False)
        top_left = (posX - textSurface.get_width()/2, posY - textSurface.get_height()/2)
        
        window.blit(textSurface,top_left)

    
    def draw(self, window): # draw function that draws all of the various parts of the game on the screen


        self.ball.draw(window)
        self.base.draw(window)
        self.printCounter(window)

        for brick in self.bricks:
            brick.draw(window)

        
