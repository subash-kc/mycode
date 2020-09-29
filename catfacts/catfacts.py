#!/usr/bin/env python3


#imports always go at the top of your code

import requests
import random

# create r, which is our request object

r = requests.get("https://cat-fact.herokuapp.com/facts")


def main():


    name_list = []

    for name in r.json()["all"]:
        if name.get("user"):
            name_list.append(f"{name['user']['name']['first']} {name['user']['name']['last']} too many names.")
    
    for x in name_list:
        print(x)




def highest_upvotes():

    upvote_list = []

    for x in r.json()["all"]:
        upvote_list.append(x.get("upvotes"))
    print("\nThe hightst upvote count was:")
    print("================")
    print(max(upvote_list))



def random_fact():
    fact_list = []

    for x in r.json["all"]:
        fact_list.append(x.get("text"))
        print("\nHave fun with a random cat fact!")
        print("==============")
        print(random.choice(fact_list))


main()
highest_upvotes()
random_fact()



