def array_diff(a, b):

    # a-b nefunguje pro listy

    a_set = set(a)
    b_set = set(b)
    return list(a_set.difference(b_set))

print(array_diff([1,2,2,2,2,2,3],[2]))