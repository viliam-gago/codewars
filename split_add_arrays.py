def split_and_add(numbers, n):

    for round in range(n):

        first, second = numbers[:len(numbers)//2], numbers[len(numbers)//2:]

        if len(first) < len(second):
            first.insert(0,0)

        new = list(map(lambda x,y: x + y,first, second))
        numbers = new

    return numbers

split_and_add([32,45,43,23,54,23,54,34], 2)