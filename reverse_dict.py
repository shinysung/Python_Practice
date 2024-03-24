# To reverse the dictionary


def reverse_dict(dict):
    new_dict = {}

    for key, value in dict.items():
        new_dict[value] = key

    return new_dict


vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principle': '원칙'
}

print("ENG-KOR vocab\n{}\n".format(vocab))

reversed_vocab= reverse_dict(vocab)
print("KOR-ENG vocab\n{}".format(reversed_vocab))