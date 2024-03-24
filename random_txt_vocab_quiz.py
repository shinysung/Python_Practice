# To create a random quiz from vocabulary.txt


import random

vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

keys = list(vocab.keys())

while True:

    index = random.randint(0, len(keys)-1)
    english_word = keys[index]
    korean_word = vocab[english_word]

    guess = input("{}: ".format(korean_word))

    if guess == 'q':
        break

    if guess == english_word:
        print("맞았습니다!")

    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))

