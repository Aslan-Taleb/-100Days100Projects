from library import * 
from logo import * 
from replit import clear

def main():
    end_game =False
    score=0
    play = ""
    C= ""
    print(logo)
    while not end_game:
        A,B = A_B(C)
        C = B
        print(f"Compare A : {A['name']}, {A['description']},from {A['country']}. ")
        print(vs)
        print(f"Against B : {B['name']}, {B['description']},from {B['country']}. ")
        while play !='a' and play!= 'b':
           play = input("\nWho has more followers ? Type 'A' or 'B' : ").lower()
        
        if more_follow(A,B,play):
            score+=1
            clear()
            print(f"You're right! Current score: {score}.\n")
        else:
            clear()
            print(logo)
            score_looser(score)
            end_game=True
        play = ""
    another_one = input("Another game ? type 'yes' or 'no' : ")
    if another_one == 'yes':
        clear()
        return False
    else:
        
        return True
            
            
        
end_programme = False    
while not end_programme:
    end_programme=main()
print("Good Bye ! ")