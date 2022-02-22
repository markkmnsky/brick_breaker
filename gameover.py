###### © Mark Kaminsky 2022. All rights reserved.

### GAMEOVER.PY = the gameover screen and scene,
# calls for the score data to be fetched via GameOverInit().returnListScores()
# and displays the score data using font and font size defined in SETUP.PY

from setup import *
from highscore_manager import GameOverInit

class GameOver:
    # static var
    color = (255,255,255)

    def update(self, deltaTime): # update function

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:# if program is closed
                return EXITEVENT # return exit event
            elif event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP: # if the user presses a key
                return STARTEVENT # return start event

    def draw(self, window): # draw function, draws all of the text
        # setting the various font sizes
        text_font = FONT_SMALL
        text_font2 = FONT_SMALLEST
        text_color = self.color
        
        
        
        # first line of text, saying "Game over"
        pos1X, pos1Y = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 80
        text_surface = text_font.render("Game over", True, text_color, None)

        top_left = (pos1X - text_surface.get_width()/2, pos1Y - text_surface.get_height()/2)
        window.blit(text_surface, top_left)


        # initializing the score variables by reading the json and doing math
        scores = GameOverInit().return_ListScores(True)
        currentScore = GameOverInit().return_ListScores(False)
        scores[:10]
        highestScore = scores[:1]
        currentScore = currentScore[:1]
        
    
        currentScore = str(currentScore)
        highestScore = str(highestScore)
        scores = str(scores)    
        
        # removing unwanted characters
        for i in ["[","]"]:
            highestScore = highestScore.replace(i, '')
            currentScore = currentScore.replace(i, '')
        for i in ["[","]"," 0,"]:
            scores = scores.replace(i, '')

        # second line of text, saying the high score
        text2_contents = "Your high score is {}".format(str(highestScore))
        
        pos2X, pos2Y = WINDOW_WIDTH /2 , (WINDOW_HEIGHT / 2) + 100
        text_surface = text_font.render(text2_contents, True, text_color, None)

        top_left = (pos2X - text_surface.get_width()/2, pos2Y - text_surface.get_height()/2)
        window.blit(text_surface, top_left)

        # sixth line of text, saying the current score
        text6_contents = "Your score is {}".format(str(currentScore))
        
        pos6X, pos6Y = WINDOW_WIDTH /2 , (WINDOW_HEIGHT / 2) + 50
        text_surface = text_font.render(text6_contents, True, text_color, None)

        top_left = (pos6X - text_surface.get_width()/2, pos6Y - text_surface.get_height()/2)
        window.blit(text_surface, top_left)


        # third line of text, saying "Press any key to play again"
        pos3X, pos3Y = (WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 150
        text_surface = text_font.render("Press any key to play again", True, text_color, None)

        top_left = (pos3X - text_surface.get_width()/2, pos3Y - text_surface.get_height()/2)
        window.blit(text_surface, top_left)

        # fourth ine of text, saying the score attempts
        pos4X, pos4Y = (WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 300
        text_surface = text_font2.render(scores, True, text_color, None)


        top_left = (pos4X - text_surface.get_width()/2, pos4Y - text_surface.get_height()/2)
        window.blit(text_surface, top_left)

        # fifth line of text, header for the score attempts saying "High Scores"
        pos5X, pos5Y = (WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 280
        text_surface = text_font2.render("High Scores:", True, text_color, None)


        top_left = (pos5X - text_surface.get_width()/2, pos5Y - text_surface.get_height()/2)
        window.blit(text_surface, top_left)








        