from replit import clear

list_bidder = {}



def add_bidder(name,price):
    list_bidder[name] = price

def who_won():
    max = 0
    winner = ""
    for key in list_bidder:
        value = list_bidder[key]
        if value> max:
            max = value
            winner = key
    print(f"The winner is '{winner}' with a bid of ${max}.")
            
        
            
            
            
        
            

            
