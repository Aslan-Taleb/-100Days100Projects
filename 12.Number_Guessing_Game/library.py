from random import * 


def select_number():
    number = randint(1,101)
    return number

def play(mode):
    if mode == "easy":
        life_easy = 10 
        game(life_easy)
    elif mode == "hard":
        life_hard = 5
        game(life_hard)
    return input("Another One ? 'y' or 'n' : ")

def win(guess,number):
    if guess == number:
        return True
    elif guess > number:
        print("Too high\n")
        return False
    elif guess < number:
        print("Too low\n")
        return False
    
def win_or_loose(guess,number):
        if win(guess,number):
            print(f"it was '{number}' you win!")
        else:
            
            print(f"no more lives,You lose! (it was {number} Looser ;))")

def game(life):
    end_game = False
    number = select_number()
    print(f"You have {life} attempts remaining to guess the number.")
    while not end_game:
        guess = int(input("Make a guess: "))
        life -= 1
        if life == 0 or win(guess,number):
            end_game = True
        else:
            print(f"You have {life} life left")
    win_or_loose(guess,number)




   
            
            
    