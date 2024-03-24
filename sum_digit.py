# Sum of digits


def sum_digit(num):
    total = 0
    str_num = str(num)

    for digit in str_num:
        total += int(digit)

    return total


# Sum of sum_digit(1) to sum_digit(1000)


total_sum = 0
for num in range(1, 1001):
    total_sum += sum_digit(num)

print(total_sum)