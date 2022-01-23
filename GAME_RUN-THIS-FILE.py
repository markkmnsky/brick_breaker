### MAIN.PY also known as GAME_RUN-THIS-FILE.PY = this file is the backbone of the game
# This is the central peice of code that calls and stems out all of the various files 
# Creates the main while loop that the name runs in, and creates the window in which the program runs in
# It would be hard to navigate the code if it was all based in one file. So, to simplify things,
# we split off all of the separate functions of the game (the code for the ball, the game logic, etc) into seperate files,
# then import them here,
# then call them when needed. 
# This improves readability significantly# 


from setup import * # setup is imported for inits and such

# the various screens are imported:
from menu import Menu 
from gameover import GameOver
from fundamental import Fundamental
from winner import Winner 

# this defines the window name, window size, window icon
program = "Brick Breaker"
icon = pygame.image.load('icon.png')
size = (WINDOW_WIDTH, WINDOW_HEIGHT)

# this sets the window size to the aforementioned defined window size, and the same for the window name, window icon
window = pygame.display.set_mode(size)
pygame.display.set_caption(program)
pygame.display.set_icon(icon)

# sets the first 'scene' to be the main menu
currentScene = Menu()

lastTime = pygame.time.get_ticks() # time system variable, needs to be initialized in order for it to start somewhere

runningStatus = True # this bool's purpose is to say that the program is running. 
# This bool is turned false if the program is closed 
# program is to close using the pygame.quit() method


while runningStatus: # while runningStatus is true, meaning the program is still 'running', run the sequence of events that compose the main while loop of the game
    window.fill((0,0,0)) # fills the window in the color of 0,0,0, which is black in RGB values

    # time system, used to keep track of time, and is used throughout the program
    # is important because it helps us figure out how long it takes for a frame to be rendered
    # variable deltaTime is super important

    currentTime = pygame.time.get_ticks() # as the while loop is cycled through, time passes, and this finds that time
    deltaTime = currentTime - lastTime # what is the difference in time between the last frame and the current frame? deltaTime is the difference in time
    lastTime = currentTime # sets last time as the current time, so when this cycles all over it knows what the last frame was

    status = currentScene.update(deltaTime) # calls the update method of whichever scene is currently running, and defines what is returned as a var
    # the 'statuses' are defined in SETUP.PY

    if status == EXITEVENT: # if the status returned by the currentScene is EXIT EVENT
        runningStatus = False # the current while loop of the game will be broken and the game will close
    elif status == STARTEVENT: # if the status returned by the currentScene is START EVENT
        currentScene = Fundamental() # the currentScene will be switched to the game logic
    elif status == GAMEOVER: # if the status returned by the currentScene is GAME OVER
        currentScene = GameOver() # the currentScene will be switched to the game over screen
    elif status == WINNINGSTATUS: # if the status returned by the currentScene is WINNING STATUS
        currentScene = Winner() # the currentScene will be switched to the winner screen

              
    currentScene.draw(window) # calls the draw method of the currentScene 
    pygame.time.wait(5) # buffer of time that restricts frame rate slightly, here for consistency reasons across computers and to prevent issues from extremely high frame rate
    
    pygame.display.update() # updates the visual of the program window after the items are drawn on the screen with currentScene.draw(window)

pygame.quit() # if the main while loop of the game logic is broken, the program is quit and closes
