#!/usr/bin/env python3


# imports always go at the top of your code

import requests


def main():

    # create r, which is our request object

    r = requests.get('http://api.open-notify.org/astros.json').json()

    print(f"People in space: {r['number']}")

    print(f"{r['people'][0]['name']} on the {r['people'][0]['craft']}")
    print(f"{r['people'][1]['name']} on the {r['people'][1]['craft']}")
    print(f"{r['people'][2]['name']} on the {r['people'][2]['craft']}")
   # print(f"People in space: {r['number']}")


def bonus():

    r =requests.get("http://api.open-notify.org/astros.json").json()

    print(f"People in space: {r['number']}")

    for astros in r['people']:
        print(f"{astros['name']} on the {astros['craft']}")

bonus()




main()
