import random


def loopsum(n):
    """Generate `n` random numbers and take their sum."""

    x = 0.

    for i in range(n):
        x += random.random()

    return x

