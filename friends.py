#!/usr/bin/env python3


character = ["messy", "serious", "creative", "sincere", "charming", "impatient"]

while True:
    response = input("Which friends character are you?").lower()

    print("You entered:", response)

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


