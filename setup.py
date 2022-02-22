###### © Mark Kaminsky 2022. All rights reserved.

### SETUP.PY = this file's purpose is to initialize Pygame and some basic variables used across every file. 
# This is helpful because it reduces unneccessary code, as we need to initialize Pygame in every file. 
# It also allows for a convinient location to store fixed variables like the screen size.
# This is helpful because those variables are used throughout to do calculations.#

import pygame # the pygame library is used as the basis for the game and is imported here

pygame.init() # pygame must be initialized to function properly

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800 # this defines the width and height of the screen in pixels, calculations are based on variables so that the screen size can be changed on demand

def aabbCheck(aabb1, aabb2): # function that checks to see if aabb can deterimine a collision
    minX1, minY1, maxX1, maxY1 = aabb1
    minX2, minY2, maxX2, maxY2 = aabb2

    if minX1 < maxX2 and maxX1 > minX2 and minY1 < maxY2 and maxY1 > minY2:
        return True

    return False
        
FONT_FILE = "font.ttf" # font file used to render text in the game, using pygame.font.Font() function

# creating variables for font sizes, so that they can be changed on demand
FONT_LARGEST = pygame.font.Font(FONT_FILE, 70)
FONT_LARGE = pygame.font.Font(FONT_FILE, 50)
FONT_NORMAL = pygame.font.Font(FONT_FILE, 30)
FONT_SMALL = pygame.font.Font(FONT_FILE, 20)
FONT_SMALLEST = pygame.font.Font(FONT_FILE, 10)


# This creates the various flags that functions in the program return when certain circumstances are met 
# i.e EXITEVENT is returned when the program is closed 
# This is necessary because it improves the readability of the code significantly.#


EXITEVENT = 0 # called when the program is closed, more specifically when the event PYGAME.QUIT is detected
STARTEVENT = 1 # called when the current scene wants to switch to the next scene, i.e the main menu switching to the game
DEADEVENT = 2 # called when the ball dies, more specifically hitting the bottom of the screen
GAMEOVER = 3 # called when the ball dies and the lives run out, initiating the game over process
WINNINGSTATUS = 4 # called when the player successfully completes all levels without running out of lives or GAMEOVER occuring


