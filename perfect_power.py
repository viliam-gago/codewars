from math import pow, fmod

def mul_power(n, k):
    x = 1

    while not fmod(pow(x,k), n) == 0:
        x += 1

    return int(pow(x,k)/n)


print(mul_power(36,2))


