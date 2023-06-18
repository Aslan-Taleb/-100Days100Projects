from library import * 
from draw import *



def main():
    test = False
    stop = False
    test_in_text = ""
    text = ""
    trash=""
    print(logo)
    while not stop:
        while not test:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            if direction == "encode" or direction == "decode":
                test = True
            else:
                print("Error : it's encode or decode.")
                
        test_in_text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        text,trash = test_text(test_in_text)
        caesar(text,shift,direction,trash)
        stop_programm = input("Type 'yes' if you want to go again,Otherwise type 'no'.\n")
        if stop_programm == "no":
            stop = True
        test = False
    print("Goodbye ! ")

main()
        





