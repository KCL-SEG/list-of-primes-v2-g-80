"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    num = 2
    while number_of_primes > 0:
        isPrime = True
        for potentialFactor in range(2, num):
            if num % potentialFactor == 0:
                isPrime = False
                break
        if isPrime:
            number_of_primes -= 1
            list.append(num)
        num += 1
    return list
