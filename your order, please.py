def order(sentence):

    if sentence:

        sentence = sentence.split(' ')
        ordered = list(range(len(sentence)))

        for word in sentence:

            for letter in word:
                if letter.isnumeric():
                    ordered[int(letter) - 1] = word

        return ' '.join(ordered)

    return ''

print(order(""))