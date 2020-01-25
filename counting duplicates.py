def duplicate_count(text):
    multiples = []
    dic = {}
    for i in text.lower():
        dic[i] = dic.get(i, 0) + 1
    [multiples.append(i) for i in dic if dic[i] > 1]
    return len(multiples)


print(duplicate_count('aaabbcdea'))
