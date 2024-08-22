#!/usr/bin/python3
"""Making change"""


def makeChange(coins: list, total):
    """determine the minimum number of coins to give while making change."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)

    count = 0
    for i in coins:
        if total >= 0:
            count += total // i
            total %= i

    return count if total == 0 else -1
