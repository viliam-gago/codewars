def spin_words(sentence):
    words = sentence.split()
    new_words = []

    nw = ' '.join([word[-1::-1] if len(word) >= 5 else word for word in words])
    return nw
    # for word in words:
    #     word = list(word)
    #     if len(word) >= 5 :
    #         word = word[-1::-1]
    #     word = ''.join(word)
    #     new_words.append(word)
    # new_words = ' '.join(new_words)
    # return new_words



print(spin_words("Hey fellow warriors"))