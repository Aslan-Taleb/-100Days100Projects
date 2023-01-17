from random import *
from game_data import *

def A_B(C):
    if C != "":
       A=C
    else: 
        A = choice(data)
    data.remove(A)
    B = choice(data)
    return A,B



def score_looser(score):
    if score < 3:
        print(f"Final score: {score}\nDid we make this too hard for you?\nThe average score is 3.2\nWe‘re pretty embarrassed for you right now.")
    elif score == 3:
        print(f"Final score: {score}\nThe average score is 3.2.\nWhat can we say... you‘re average!\nGet a score over 8 and you would be in the top 10% of players.\nStay focussed...")
    elif score >= 8:
        print(f"Final score: {score}\nyou're better than 90% of people at this game..but hey, that's not what will make you find a job\n here for you : 'www.pole-emploi.fr'.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        
             
        



def more_follow(A,B,game):
    if A['follower_count'] >= B['follower_count']:
        return game == "a"
    else:
        return game == "b"
       
        
    


