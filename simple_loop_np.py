import numpy as np
import time


VEC_SIZE = 1000
NUM_RUNS = 10**6


u = np.random.randint(1, 1000, VEC_SIZE)
v = np.random.randint(1, 1000, VEC_SIZE)

start = time.time()
for i in range(NUM_RUNS):
    np.sum(u * v)
end = time.time()
print(f"{end - start}")
