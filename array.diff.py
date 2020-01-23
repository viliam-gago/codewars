def array_diff(a, b):

    for numberb in b:
        while numberb in a:
            a.remove(numberb)
    return a

print(array_diff([1,2,2,2,2,2,3],[2]))