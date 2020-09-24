#!/usr/bin/env python3




def function(x, y):

    print(x + y)
    return


def substract(x, y):

    print(x -y)

    return

def multiply(x, y):

    print(x * y)

    return

def divide(x, y):

    print(x/y)

    return

print("1.Addition")

print("2.Substract")

print("3.Multiply")

print("4.Divide")

x = float(input("Enter the first number: "))

y = float(input("Enter the second number: "))

response = int(input("made your selection. 1/2/3/4: "))

if response == 1:
    add(x, y)
elif response == 2:
    substract(x, y)

elif response == 3:
    multiply(x, y)

elif response == 4:
    divide(x, y)

else:
    print("Invalid Syntax")



