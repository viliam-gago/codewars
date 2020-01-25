def find_even_index(arr):
    sum_left = 0
    sum_right = 0

    for i in range(len(arr)):
        for j in range(-1,-len(arr)+i,-1):
            sum_right += arr[j]
        if sum_left == sum_right:
            return i
        sum_left += arr[i]
        sum_right = 0
    return -1





print(find_even_index([-100,-1]))