# To reverse the list


numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers) // 2):
    right = len(numbers) - left - 1
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("reversed list: " + str(numbers))
