from setup import *

class Menu:

    color = (255,255,255)
    background = (0,0,0)

    def __init__(self):
        self.text1 = "Brick Breaker"
        self.text2 = "Press any key to start"

    def update(self, deltaTime):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXITEVENT
            elif event.type == pygame.KEYUP:
                return STARTEVENT

    
    def draw(self, window):
        text_font = FONT_SMALL
        posX, posY = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        
        textSurface2 = text_font.render(
            self.text1,
            True, 
            self.color,
            None
        )

        top_left = (posX - textSurface2.get_width()/2, posY - textSurface2.get_height()/2)
        window.blit(textSurface2, top_left)
        
        textSurface2 = text_font.render(
            self.text2,
            True, 
            self.color,
            None
        )

        top_left = (posX - textSurface2.get_width()/2, (posY + 60) - textSurface2.get_height()/2)
        window.blit(textSurface2, top_left)
