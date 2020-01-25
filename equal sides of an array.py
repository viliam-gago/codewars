def find_even_index(arr):
    sum_left = 0
    sum_right = 0
    pairs = []
    indexes = []

    for i in range(len(arr)):
        sum_left += arr[i]
        for j in range(-1,-len(arr)-1,-1):
            sum_right += arr[j]
            print("suma zprava:",sum_right)
            print("suma zleva:",sum_left)
            print('\n')
            if sum_right == sum_left:
                pairs.append([sum_left,sum_right])
                indexes.append(arr.index(arr[i]))


        sum_right = 0
        print('\n=================== DALSI PRICTENI ZLEVA ==========================\n')

    print(pairs)
    print(indexes)

print(find_even_index([1,2,3,4,3,2,1]))