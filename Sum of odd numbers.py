def row_sum_odd_numbers(n):
    sum = 0 
    for i in range(n):
        sum += i
    start = sum * 2 + 1
    end = start + (n - 1) * 2
    total = 0
    for i in range(start, end + 1, 2):
        total += i
    print(str(start) + " " + str(end))
    return total
print(row_sum_odd_numbers(13))

