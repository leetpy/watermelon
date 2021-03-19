from random import randint


def sample(population, k):
    result = [None] * k
    pool = list(population)
    n = len(population)
    for i in range(k):
        j = randint(0, n-i)
        result[i] = pool[j]
        pool[j] = pool[n-i-1]

    return result
