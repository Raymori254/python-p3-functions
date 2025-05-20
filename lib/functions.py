#!/usr/bin/env python3
def my_function(param):
    print("Running my_function")
    return param + 1

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    
    pass

def add(num1, num2):
    print("add(num1, num2)")
    return num1 + num2
    pass

def halve(number):
    print("halve(number)")
    if number == 0:
        return None
    else:
        return number / 2
    pass


