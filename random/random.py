#!/usr/bin/env python3



while True:
    response = int(input("How many days are there in a leap year? "))
    print("You entered:", response)
    
    if response == 366 :
        print("You have cleared the first level.")
        response = input("What month has an extra day in leap year?? ").lower()
        if response == "february" :
            print("You have cleared the test.")
            break
        else :
            print("You have failed the test.")
            break
    else :
        print("Your input is wrong, please try again.")





while True:
    response = input("Which Python data type is an ordered sequence? ").lower()
    print("You entered:", response)
    
    if response == "list" :
        print("You have cleared the test.")
        break
    elif response == "tuple" :
        print("You have cleared the test.")
        break
    else :
        print("Your input is wrong. Please try again.")

