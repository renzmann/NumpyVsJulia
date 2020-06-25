import os
from os.path import abspath, join, exists
import time
import numpy as np
import itertools
import pandas as pd


VEC_SIZE = 10**4
NUM_RUNS = 10**6


def make_u_v(vec_size=VEC_SIZE):
    u = np.random.rand(vec_size)
    v = np.random.rand(vec_size)
    return u, v


def run(u, v, num_runs):
    start = time.time()
    for i in range(num_runs):
        u @ v
    end = time.time()
    return end - start


def main():

    u, v = make_u_v()
    result = run(u, v, NUM_RUNS)
    print(result)


if __name__ == '__main__':
    main()
