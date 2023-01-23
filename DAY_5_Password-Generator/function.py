import random as r

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def randomCharacters_EZ(type,nmbr):
    password = ""
    for i in range(0,nmbr):
        password += r.choice(type)
    return password
    
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def ez(nr_letters,nr_symbols,nr_numbers):
    password = ""
    password += randomCharacters_EZ(letters,nr_letters)
    password += randomCharacters_EZ(symbols,nr_symbols)
    password += randomCharacters_EZ(numbers,nr_numbers)
    print(f"EZ Password : {password}")
    
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def hard(nr_letters,nr_symbols,nr_numbers):
    chaine_password = []
    password_hard = ""
    chaine_password += randomCharacters_EZ(letters,nr_letters)
    chaine_password += randomCharacters_EZ(symbols,nr_symbols)
    chaine_password += randomCharacters_EZ(numbers,nr_numbers)
    r.shuffle(chaine_password)
    for char in chaine_password:
        password_hard += char
    print(f"Hard Password : {password_hard}")
    
    
    
    
intro = ('''
                                    ████████                
                                ████▒▒    ▒▒████            
                              ██▓▓            ████          
                          ▒▒██                  ████        
                          ██                      ██        
                  ████  ██▒▒                        ██      
              ██▓▓    ▓▓██                          ██      
            ██                                      ██      
            ██            ▒▒██████▓▓                ██      
          ██            ██          ██              ████    
          ██          ██    ██████▒▒  ██                ██  
      ██████        ██  ▓▓██      ████  ██                ██
    ██▓▓            ██  ██          ██  ██                ██
  ████              ██  ██          ██  ██                ██
  ██                ██  ██          ██  ██                ██
  ██                ██  ██          ██  ██                ██
  ██              ██████████████████████████            ██  
    ██          ██                          ██        ████  
      ████████████                          ██████████      
                ██          ██████          ██              
                ██          ██  ██          ██              
                ██          ██████          ██              
                ██            ██            ██              
                ██            ██            ██              
                ██                          ██              
                ██                          ██              
                ████████████████████████████▓▓  
         ''')
