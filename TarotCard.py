 #!/usr/bin/env python
# coding: utf-8

import csv
import random

# - Cups: Cups represent emotions, relationships, intuition, and the subconscious mind. They are associated with the element of water, which symbolizes fluidity, intuition, and the depths of the unconscious.
# - Pentacles: Pentacles represent the material world, including finances, career, health, and physical manifestations of abundance. They are associated with the element of earth, which signifies stability, practicality, and the tangible aspects of life.
# - Swords: Swords represent the intellect, thoughts, communication, and challenges related to the mind. They often signify conflict, mental clarity, decision-making, and the power of perception. Swords are associated with the element of air, symbolizing intellect, communication, and swift action.
# - Wands: Wands represent creativity, passion, inspiration, and spiritual energy. They are associated with the element of fire, symbolizing transformation, vitality, and the spark of innovation or growth.

def read_cards():
    with open("./data/tarot.csv") as file:
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
        print(q)
        input(".")

        c = card[1]
        cn = c['Card']
        cs = c['Summary']
        cd = c['Details']
        print("  (", cn, ") ", cs, "\n    ", cd)
        input(".")

tarot()
