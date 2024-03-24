# To create a quiz from vocabulary.txt

with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]

        guess = input("{}: ".format(korean_word))

        if guess == english_word:
            print("Correct!\n")
        else:
            print("Unfortunately, the answer is {}.\n".format(english_word))