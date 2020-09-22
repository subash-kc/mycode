#!/usr/bin/env python3

message = 'The movie is about to begin, we recommend '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 25:
    message = message + 'setting video to 4k.'
elif connection >= 5:
    message = message + 'setting video to 1080p.'
elif connection >= 2:
    message = message + 'setting video to 720p.'
else:
    message = message + 'finding another access network.'
print(message)

while True:
    response = input("Which friends character are you?").lower()

    print("You entered:", response)

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



