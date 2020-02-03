def tribonacci(signature, n):

    while len(signature) < n:
        signature.append(sum(signature[-1:-4:-1]))

    return signature[0:n]


print(tribonacci([1, 1, 1], 10))