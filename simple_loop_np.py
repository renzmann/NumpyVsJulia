import time
import numpy as np


VEC_SIZE = 1000
NUM_RUNS = 10**6


u = np.random.randint(1, 1000, VEC_SIZE)
v = np.random.randint(1, 1000, VEC_SIZE)

start = time.time()
for i in range(NUM_RUNS):
    u @ v
end = time.time()
print(f"{end - start}")
