import timeit

setup = """
import numpy as np

def loopsum(n):
    return np.random.rand(n).sum()
"""

num_runs = 10**3
time = timeit.timeit("loopsum(10**6)", setup=setup, number=num_runs) / num_runs
print("Mean time: {:,.3f} ms".format(time * 1e3))
