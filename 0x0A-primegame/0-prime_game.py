#!/usr/bin/python3
"""Prime Game"""


def generate_primes(num):
    """Generate prime numbers up to num using the Sieve of Eratosthenes"""
    if num < 2:
        return []
    sieve = [True] * (num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    primes = []

    for i in range(2, num + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, num + 1, i):
                sieve[j] = False

    return primes


def isWinner(x, nums):
    """Find the winner between Maria and Ben"""
    if x < 1 or nums is None:
        return None

    maria = ben = 0

    for num in nums:
        primes = generate_primes(num)
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben == maria:
        return None
    return "Ben" if ben > maria else "Maria"
