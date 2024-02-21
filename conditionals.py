# Simple conditionals

# name = input("enter your name:")
# print(type(name))
# age = int(input("enter your age:"))
# print(type(age))

# if age > 18 or len(name) > 5:
#     print(f"hello {name}, you are an adult")
# elif (age > 12):
#     print(f"hello {name}, you are an teen")
# else:
#     print(f"hello {name}, you are an child")

# if (True):
#     print("something")


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



