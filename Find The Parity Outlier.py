def find_outlier(integers):
    odd = []
    even = []

    for number in integers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    if len(even) > len(sum_odd):
        return odd[0]
    else:
        return even[0]


print(find_outlier([2, 4, 6, 8, 10, 3]))
