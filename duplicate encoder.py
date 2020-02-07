def duplicate_encode(word):
    counts = {}

    for i in word.lower():
        counts[i] = counts.setdefault(i, 0) + 1

    return ''.join([')' if counts[i] > 1 else '(' for i in word.lower()])


print(duplicate_encode('Success'))
