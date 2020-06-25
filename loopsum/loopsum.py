import timeit

setup = """
import random

def loopsum(n):
    x = 0.
    for i in range(n):
        x += random.random()
    return x
"""

num_runs = 50
time = timeit.timeit("loopsum(10**6)", setup=setup, number=num_runs)
print("Mean time: {:,.3f} ms".format(time * 1e3))
