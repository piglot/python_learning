#!/usr/bin/python3

## Get an odd number iterator:
## 3 5 7 9 11 13 15 17...
def odd_iter():
    n = 3
    while True:
        yield n
        n = n + 2

## Return those divisible numbers
def not_divisible(n):
    return lambda x:x%n > 0

## Get a prime number iterator
def primes():
    yield 2
    it = odd_iter()
    for i in it:
        yield i
        it = filter(not_divisible(i), it)

## Test to get primes < 100
for i in primes():
    if i < 100:
        print(i)
    else:
        break
