###### © Mark Kaminsky 2022. All rights reserved.

### MENU.PY = the main menu screen and scene,
# and displays lines of text using font and font size defined in SETUP.PY 

from setup import *

class Menu:

    # defining static var
    color = (255,255,255)
    background = (0,0,0)

    def __init__(self):
        # the text values of the lines of text
        self.text1 = "Brick Breaker"
        self.text2 = "Use scroll wheel to control"
        self.text3 = "Press any key to start"

    def update(self, deltaTime): # update method

        for event in pygame.event.get(): # checks event status
            if event.type == pygame.QUIT: # if program is closed
                return EXITEVENT # returns exit event
            elif event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP: # if user presses key
                return STARTEVENT # start event

    
    def draw(self, window): # draw lines of text on screen
        text_font = FONT_SMALL
        posX, posY = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        
        # 1st line of text
        textSurface1 = text_font.render(
            self.text1,
            True, 
            self.color,
            None
        )

        top_left = (posX - textSurface1.get_width()/2, posY - textSurface1.get_height()/2)
        window.blit(textSurface1, top_left)
        
        # second line of text
        textSurface2 = text_font.render(
            self.text2,
            True, 
            self.color,
            None
        )

        top_left = (posX - textSurface2.get_width()/2, (posY + 60) - textSurface2.get_height()/2)
        window.blit(textSurface2, top_left)
        

        # third line of text   
        textSurface3 = text_font.render(
            self.text3,
            True, 
            self.color,
            None
        )

        top_left = (posX - textSurface3.get_width()/2, (posY + 120) - textSurface3.get_height()/2)
        window.blit(textSurface3, top_left)
