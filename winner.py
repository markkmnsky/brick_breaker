### WINNER.PY = the winner screen and scene, 
# and displays lines of text using font and font size defined in SETUP.PY

from setup import *

class Winner:

    # defining static var
    color = (255,255,255)
    background = (0,0,0)

    def __init__(self):
        # defining lines of text
        self.text1 = "You win!"
        self.text2 = "Congratulations!"
        self.text3 = "Press any key to start"

    def update(self, deltaTime): # same as MENU.PY

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXITEVENT
            elif event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                return STARTEVENT

    
    def draw(self, window): # same as MENU.PY
        text_font = FONT_SMALL
        posX, posY = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        
        textSurface1 = text_font.render(
            self.text1,
            True, 
            self.color,
            None
        )

        top_left = (posX - textSurface1.get_width()/2, posY - textSurface1.get_height()/2)
        window.blit(textSurface1, top_left)
        
        textSurface2 = text_font.render(
            self.text2,
            True, 
            self.color,
            None
        )

        top_left = (posX - textSurface2.get_width()/2, (posY + 60) - textSurface2.get_height()/2)
        window.blit(textSurface2, top_left)
        
        
        textSurface3 = text_font.render(
            self.text3,
            True, 
            self.color,
            None
        )

        top_left = (posX - textSurface3.get_width()/2, (posY + 120) - textSurface3.get_height()/2)
        window.blit(textSurface3, top_left)
