# To Replace all vowel to exclamation mark in the sentence


def replace_exclamation(st):
    vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    list_st = []

    for i in str(st):
        if i in vowel:
            st = st.replace(i, "!")

    return st


# Test code


print(replace_exclamation("HI!"))
print(replace_exclamation("!HI! Hi!"))
print(replace_exclamation("aeiou"))
print(replace_exclamation("ABCDE"))