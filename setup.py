import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800

def aabbCheck(aabb1, aabb2):
    minX1, minY1, maxX1, maxY1 = aabb1
    minX2, minY2, maxX2, maxY2 = aabb2

    if minX1 < maxX2 and maxX1 > minX2 and minY1 < maxY2 and maxY1 > minY2:
        return True

    return False
        
FONT_FILE = "font.ttf"

FONT_LARGEST = pygame.font.Font(FONT_FILE, 70)
FONT_LARGE = pygame.font.Font(FONT_FILE, 50)
FONT_NORMAL = pygame.font.Font(FONT_FILE, 30)
FONT_SMALL = pygame.font.Font(FONT_FILE, 20)
FONT_SMALLEST = pygame.font.Font(FONT_FILE, 10)

EXITEVENT = 0
STARTEVENT = 1





