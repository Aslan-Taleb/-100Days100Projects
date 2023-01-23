from replit import clear
from math import *

def add(x,y):
    return x+y
 
def substract(x,y):
    return x-y
 
def multiply(x,y):
    return x*y 
 
def divide(x,y):
    return x/y
def power(x,y):
    return x**y


operation = {}
operation['+'] = add
operation['-'] = substract
operation['*'] = multiply
operation['/'] = divide
operation['**'] = power


def loop_operation():
    for i in operation:
        print(i)
        
def make_operation(new_operation,result):
    if new_operation:
        first = float(input("What's the first number? : "))
        loop_operation()
    else:
        first = result
    myOperation = (input("Pick an operation : "))
    myFunction= operation [myOperation]
    second = float(input("What's the second number? : "))
    result = round(myFunction(first,second),2)
    print(f"{first} {myOperation} {second} = {result}")
    return result