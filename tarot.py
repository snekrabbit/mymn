import csv
import os
import random

def read_cards():
    path = os.path.expanduser("~/data/tarot.csv")
    with open(path) as file:
        row_reader = csv.DictReader(file)
        cards = []
        for card in row_reader:
            cards.append(card)
        return cards

def choose_cards(cards, n):
    choice = random.sample(cards, n)
    return choice

Q3 = [
    "What is energizing me?", 
    "Where can I expect to need grace?", 
    "What should I take a closer look at?"
]
def read_3():
    deck = read_cards()
    choice = choose_cards(deck, 3)
    return [
        [Q3[0], choice[0]],
        [Q3[1], choice[1]],
        [Q3[2], choice[2]]
    ]

def tarot():
    spread = read_3()
    print("Welcome to your future!")
    print()
    for card in spread:
        q = card[0]
        c = card[1]
        cn = c['Tarot Card']
        cd = c['Meaning']
        print(q)
        print("  (", cn, ") ", cd)
        print()
        input()

tarot()
