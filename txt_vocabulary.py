# To create a vocabulary.txt
# Press q to exit


with open('vocabulary.txt', 'w') as f:
    while True:
        english_word = input("Enter an English word: ")
        if english_word == 'q':
            break

        korean_word = input("Enter a Korean word: ")
        if korean_word == 'q':
            break

        f.write("{}: {}\n".format(english_word, korean_word))
