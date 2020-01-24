def find_outlier(integers):

    sum_odd = 0
    sum_even = 0

    for number in integers:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    return min(sum_odd, sum_even)

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
