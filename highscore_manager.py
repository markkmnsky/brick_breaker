### HIGHSCORE_MANAGER.PY = deals with the process of saving and reading scores to high_scores.json 
from setup import *

import json



def write_json(new_data, filename ="high_scores.json"): # write json function, writes and appends provided new_data into the json file
    with open(filename, 'r+') as file: # opens the file
        file_data = json.load(file) # loads the file as python info
        file_data["details"].append(new_data) # appends into the data
        file.seek(0) 
        json.dump(file_data, file, indent=4) # writes the data back into the json




class GameOverInit:

    def update_NewScore(self, scoreCounter): # update the score function with provided score counter
        info = { # creates the style of the into inside the json file
            "score" : scoreCounter
        }       
        write_json(info) # calls the write json function

    def return_ListScores(self, sorted): # return list scores, has option to sort the results or simply return them as they are (flipped though)
        scoreList = [] # creates empty list
        filename = "high_scores.json"
        with open(filename) as file: # opens file
            data = json.load(file) # loads the file as python info
            for detail in data["details"]: # searches for the heading "details"
                for score in [detail["score"]]: # then searches for the detail's assosiated score
                    scoreList.append(score) # appends the score to the list
        
        if sorted == True: # if asked to sort
            scoreList.sort(reverse=True) # sorts
        elif sorted == False: # if is not asked to sort
            scoreList.reverse() # still reverses the list so that it follows chronological order
        return scoreList # returns final list


#debug
#print(GameOverInit().return_ListScores(False))