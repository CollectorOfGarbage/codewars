def binary_array_to_number(arr):
    power = len(arr) - 1
    sum = 0
    for i in arr:
        sum += i * 2 ** power
        power -= 1
    return sum



binary_array_to_number([1,1,0,0,1])