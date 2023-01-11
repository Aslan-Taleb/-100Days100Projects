
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text,shift):
    shift = shift % 26
    coded = ""
    on_the_other_side = False
    overflow = ""
    for letter in text:
        myIndex=alphabet.index(letter)
        if myIndex+shift <= len(alphabet)-1:
            coded+=alphabet[myIndex+shift]
        else:
            i=0
            while not on_the_other_side:
                overflow=alphabet[myIndex+i]
                i+=1
                if overflow == 'z':
                    on_the_other_side = True
            coded+=alphabet[shift-i]
        on_the_other_side = False
    return coded


def decrypt(text,shift):
    shift = shift % 26
    decoded = ""
    on_the_other_side = False
    overflow = ""
    for letter in text:
        myIndex=alphabet.index(letter)
        if myIndex-shift >= 0:
            decoded+=alphabet[myIndex-shift]
        else:
            i=0
            while not on_the_other_side:
                overflow=alphabet[myIndex-i]
                i+=1
                if overflow == 'a':
                    on_the_other_side = True
            decoded+=alphabet[(len(alphabet)-1)-(shift-i)]
            on_the_other_side = False
         
    return decoded




def caesar(text,shift,direction):
    message = ""
    result = 0
    
    if direction == "encode":
        result = encrypt(text,shift)
        print("Your message encrypt (by Cesar himself ! ) : "+result+"\n")
    elif direction == "decode":
        result = decrypt(text,shift)
        print("Your message decrypt (by Cesar himself ! ) : "+result+"\n")
    