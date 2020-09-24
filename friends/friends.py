#!/usr/bin/env python3


response = ["serious", "messy", "impatient", "charming", "sincere", "creative"] 

while True:
    character = input("Which friends character are you?").lower()

    print("You entered:", character)

#friends = ["Rachel", "Ross", "Monica", "Chandler", "Joey", "Pheobe"]
if response == "messy":
    print("You are Phoebe.")
    break

elif response == "serious":
    print("You are Monica.")
    break


elif response == "creative":
    print("You are Ross.")
    break

elif response == "impatient":
    print("You are Joey.")
    break

elif response == "sincere":
    print("You are Chandler.")
    break

elif response == "charming":
    print("You are Rachel.")
    break

else:
    print("You are just a normal person.")


