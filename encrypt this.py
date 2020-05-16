import string

def encrypt_this(text):
    text_l = text.split()

    new = ''

    for word in text_l:

        if len(word) == 1:
            first = str(ord(word[0]))
            new += first + ' '

        elif len(word) == 2:
            first = str(ord(word[0]))
            new += first + word[1] + ' '

        elif len(word) == 3:
            first = str(ord(word[0]))
            second = word[1]
            last = word[-1]
            new += first + last + second + ' '

        else:
            first = str(ord(word[0]))
            second = word[1]
            middle = word[2:-1]
            last = word[-1]

            new += first + last + middle + second + ' '



    return new.rstrip()


print(encrypt_this('A wise old owl lived in an oak'))


