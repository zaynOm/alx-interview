#!/usr/bin/python3
"""Prime Game"""


def generate_primes(num):
    """generate prime numbers up to num"""
    nums = primes = []
    if num > 2:
        nums = [2] + list(range(3, num + 1, 2))
    for i in nums:
        for j in range(2, i + 1):
            if j > i / 2:
                primes.append(i)
                break
            if i % j == 0:
                break
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
    res = "Ben" if ben > maria else "Maria"
    return res
