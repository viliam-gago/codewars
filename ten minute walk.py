def is_valid_walk(walk):

    directions = {'n': -11, 's': 11, 'w': -1, 'e': 1}
    track = [directions[i] for i in walk]

    if len(walk) == 10 and sum(track) == 0:
        return True


    else:
        return False





print(is_valid_walk(['w', 'w', 's', 'n', 'e', 'e', 'n', 's']))