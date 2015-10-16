#!/usr/bin/python

from itertools import combinations

prices = {
    1: 8,
    2: 15.2,
    3: 21.6,
    4: 25.6,
    5: 30,
}

def potter(books):
    items = set(books)
    final = len(books) * 8

    for amount in range(1,len(items)+1):
        for combination in combinations(items, amount):
            remainder = books[:]
            for x in combination:
                remainder.remove(x)
            price = prices[amount] + potter(remainder)
            if price < final:
                final = price

    return final

if __name__ == '__main__':
    assert potter([]) == 0
    assert potter([1]) == 8
    assert potter([1, 2]) == 15.2
    assert potter([1, 2, 3]) == 21.6
    assert potter([1, 2, 3, 4]) == 25.6
    assert potter([1, 2, 3, 4, 5]) == 30
    assert potter([1, 2, 3, 4, 5, 1, 2, 3]) == 51.2
