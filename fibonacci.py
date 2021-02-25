def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def factor(n):
    fact = 1
    for i in range(1, n + 1) :
        fact = fact * i

    return fact


print(factor(3))
