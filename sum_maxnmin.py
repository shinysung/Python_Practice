# To sum all the numbers of a given array, except the highest and the lowest element.


def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0

    return sum(arr) - max(arr) - min(arr)

# Test code

print(sum_array([6, 2, 1, 8, 10]))


