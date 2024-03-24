# To print times table


a = 1 # row
while a < 10:
    b = 1 # column
    while b < 10:
        print("{} * {} = {}".format(a, b, a * b))
        b += 1
    a += 1

