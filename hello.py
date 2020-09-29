#!/usr/bin/python3

print("""Author: Subash HC

Date: 2020-09-23""")



import os

from playsound import playsound

print("\nHello World")



print("""\nTwinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.\n""")


#playsound('Users/msubash213/Desktop/play.mp3')

print(os.listdir())


# logical operaters

bool1 = True

bool2 = False

print("\nThe value of not boool 2 is ", (not bool2))

 #Type Casting --> is a way to conver one data type to another.

a = "3534"

a = int(a)

print(a + 10)

name = input("\nEnter your name: ")
print(name)

num1 = 200

num2 = 500

print("\nThe sum of two numbers is ", (num1 + num2))

num3 = 43

print("\n The remainder is when num3 is divide by 2 is ", num3%2)



num = input("Enter a number: ")

print(type(num))


x = input("Enter a first number: ")

y = input("Enter a second number: ")

x = int(x)

y = int(y)

avg = (x+y)/2


print("\n The average value of x and y", avg)




































