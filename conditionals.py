# Simple conditionals

"""
    I’ve put the code into functions to make it easier to work with.
    Functions are essentially blocks of code that execute when the function is called. 
    To run the code, you call the function at the beginning of a new line, under* the function block.

    Here’s an example:

get_input()

"""
def get_input():
        
    name = input("enter your name:")
    print(type(name))
    age = int(input("enter your age:"))
    print(type(age))

    if age > 18 or len(name) > 5:
        print(f"hello {name}, you are an adult")
    elif (age > 12):
        print(f"hello {name}, you are an teen")
    else:
        print(f"hello {name}, you are an child")


def calculator():
    num1 = int(input("num:"))
    num2 = int(input("num2:"))
    op = input("write your opperator:")


    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("undefined")
        else:
            print(num1 / num2)
    else:
        print(num1 % num2)



