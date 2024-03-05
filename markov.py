import json
import random
import re

TI = "./data/treasure-island.txt"
SL = "./data/small-lamb.txt"

def file_words(f):
    with open(f) as file:
        all = file.read()
        all = all.lower()
        all = re.sub(r'[^\'a-z]', ' ', all)
        return all.split()

# W_WORDS = {word: {nextWord: count}}
W_WORDS = {}

def index(f):
    prior = None
    words = file_words(f)
    words.append(words[0])
    for word in words:
        if prior:
            # remember prior+word
            next_words = W_WORDS.get(prior, [])
            next_words.append(word)
            W_WORDS[prior] = next_words

        # remember it for the next iteration
        prior = word

def generate(n):
    # pick a random first word of the sentence
    all_words = list(W_WORDS.keys())
    rand_word_ix = random.randint(0, len(all_words)-1)
    first = all_words[rand_word_ix]
    sentence = [first]

    # add the next N-1 random words most likely to follow
    for i in range(n-1):
        next_words = W_WORDS[sentence[-1]] 
        next_ix = random.randint(0, len(next_words)-1) 
        next = next_words[next_ix] 
        sentence.append(next)

    return " ".join(sentence)

index(TI)
#print(json.dumps(W_WORDS))
print(generate(50))
