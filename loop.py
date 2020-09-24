#!/usr/bin/env python3


# For every [dish] I find in the [sink] I 'm going to [scream]


room= ["bowl", "fork", "plates", "mug"]

for dish  in room:

         print(f"\nThere's a {dish} in the room, I'm going to whoop your ass.")



room= ["kitchen", "toilet", "master room", "living room", "balcony"]


for light in room:

    print(f"\nThere's a {light}'s light on, I'm going to take a dollar!")


reportcard = ["Science", "Mathematics", "Social Studies", "Population", "Health Education", "English"]


for A in reportcard:

    print(f"\nif there's a A in {A}'s reportcard, I'm going to give you a new video game to the collection")

#For every [dirty dish] I find in your [room], that's how many times I'm going to [whoop your ass].


room = ["bed", "table", "laptop", "curtain", "glass", "luggage", "plate", "bowl", "lamp"]

dish = ["glass", "plate", "bowl"]


print(f"\nGrandma takes dirtydishes seriously and you should too!")

for dish in room:
    if dish == "room":
        number = number + 1
        print(f"Oh you didn't, that's a dirtydishes number {number}, I am going to whoop your ass")

room = ["light_on", "light_off", "light_on", "light_off", "light_off", "light_on"]

dollars = 10


print(f"\nGrandma is about to start her rounds, you have ${dollars} so far, she'll be take one dollar for every light that is on in the room.")

for light in room:
    if light =="light_on":
        dollars = dollars -1
        print(f"that's another light, you now have ${dollars}! ")


#For every [A] I find in your [report card] I'm going to give you a new [video game] for your {collection}.


report_card = ["A", "B", "F", "C" "A", "A", "F", "A", "A"]
video_game = 8

for grade in report_card:
    if grade == "A":
        video_game = video_game + 1

        print(f"\n Well, you got another A, you now have {video_game} in your game collection.")











