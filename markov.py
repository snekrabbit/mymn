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

# W_COUNTS = {word: countOfNextWords}
W_COUNTS = {}

def index(f):
    prior = None
    words = file_words(f)
    words.append(words[0])
    for word in words:
        if prior:
            # remember prior+word
            next_words = W_WORDS.get(prior, {})
            num_next = next_words.get(word, 0)
            next_words[word] = num_next + 1
            W_WORDS[prior] = next_words

            c = W_COUNTS.get(prior, 0)
            W_COUNTS[prior] = c + 1

        # remember it for the next iteration
        prior = word
#print(json.dumps(W_WORDS))

def generate(n):
    rand_ix = random.randint(0, len(W_WORDS)-1)

    prior = list(W_WORDS.keys())[rand_ix]
    all = [prior]
    for i in range(n):
        next_words = W_WORDS[prior]
        next_ix = random.randint(0, len(next_words)-1)
        next = list(next_words.keys())[next_ix]
        all.append(next)
        prior = next
        i = i+1
        if i>n:
            break
    return " ".join(all)

index(SL)
print(generate(25))
