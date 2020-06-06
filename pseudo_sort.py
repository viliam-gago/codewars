def pseudo_sort(st):

    li = list(map(lambda y: ''.join(filter(lambda x: x.isalnum(), y)), string.split(' ')))

    low =[]
    up = []

    for word in li:
        if word.islower():
            low.append(word)
        else:
            up.append(word)

    return ' '.join(sorted(low) + sorted(up,reverse=True))



string = "I, habitan of the Alleghanies, treating of him as he is in himself in his own rights"
print(pseudo_sort(string))