#Made by AslaN
from art import *
from words_function import * 


print(logo)
Language = -1
while Language!=1 and Language != 2:
    Language = int(input("English (1) Or French (2) ? "))
    
if Language == 1:
    chosen_word = random.choice(word_english_list)
    
else:
    chosen_word = random.choice(word_french_list)



display = []
display_loser = []
live = 6
guess = ""

for i in range(0,len(chosen_word)):
    display+="_"
print(ListToStr(display))

    

end_of_game = False



while not end_of_game:
    position = 0
    not_in = 0
    guess = input("Guess a letter: ").lower()
    
    #clear()
    while guess in display_loser:
        print(f"You've already tried {guess} and It's not in the word.")
        guess = input("Guess a letter: ").lower()
        
    if guess in display:
        print(f"You've already guessed {guess}")
    
    
    for letter in chosen_word:
        if letter == guess:
            display[position] = letter   
        else:
            not_in+=1
        position+=1
    if not_in == position:
        live-=1
        print(f"You guessed {guess},that's not in the word.You lose a life. ")
        print(stages[live])
        display_loser.append(guess)
    print(ListToStr(display))
    


    if "_" not in display or live == 0:
        end_of_game = True
    
        
        
        
        
        
        
        
        
        
if live ==0:
    print("You Lose.")
    print(f"The word was :  {chosen_word}")
else:
    print("You Win.")




