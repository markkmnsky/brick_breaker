from menu import Menu
from setup import *
from fundamental import Fundamental


program = "Brick Breaker"
icon = pygame.image.load('icon.png')

runningStatus = True

size = (WINDOW_WIDTH, WINDOW_HEIGHT)
window = pygame.display.set_mode(size)
pygame.display.set_caption(program)
pygame.display.set_icon(icon)

currentScene = Menu()

lastTime = pygame.time.get_ticks()



while runningStatus:
    window.fill((0,0,0))

    currentTime = pygame.time.get_ticks()
    deltaTime = currentTime - lastTime
    lastTime = currentTime


    status = currentScene.update(deltaTime)
    currentScene.draw(window)           

    if status == EXITEVENT:
        runningStatus = False
    elif status == STARTEVENT:
        currentScene = Fundamental()

    pygame.time.wait(5)
    
    pygame.display.update()

pygame.quit()
