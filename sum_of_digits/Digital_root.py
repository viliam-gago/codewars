def digital_root(n):

    while len(str(n)) >= 2:
        suma = 0
        for digit in str(n):
            suma += int(digit)
        n = suma
    return n

print(digital_root(132189))