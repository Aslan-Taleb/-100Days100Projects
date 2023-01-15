from logo import * 
from library import * 
def main():
    new_operation = True
    result = 0
    print(logo)
    while True:
        result = make_operation(new_operation,result)
        ask = input(f"Type 'y' to continue calculating with {result},or type 'n' to start a new calculation : ")
        if ask == 'y':
            new_operation = False
        else:
            new_operation = True
            clear()
        
main()
    
    