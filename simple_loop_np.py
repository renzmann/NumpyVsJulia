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
    vec_sizes = [10**i for i in range(9, 10)]
    run_lengths = [10**i for i in range(0, 1)]
    combinations = itertools.product(vec_sizes, run_lengths)
    run_data = []

    for vec_size, num_runs in combinations:
        print(f"Running combination: `vec_size`={vec_size} ..."
              f" `num_runs`={num_runs}", flush=True, end='\r')
        u, v = make_u_v(vec_size)
        run_data.append([vec_size, num_runs, run(u, v, num_runs)])

    out_dir = abspath(join(os.getcwd(), 'data'))
    out_file = join(out_dir, 'python_runs.csv')
    if not exists(out_dir):
        os.makedirs(out_dir)
    print(f"\nSaving data to {out_file}")
    run_df = pd.DataFrame(run_data, columns=['vec_size', 'num_runs', 'runtime'])
    run_df.to_csv(out_file, index=False)


if __name__ == '__main__':
    main()
