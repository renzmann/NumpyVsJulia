import time
import random


VEC_SIZE = 1000
NUM_RUNS = 10**6


u = [random.randint(1, 1000) for i in range(VEC_SIZE)]
v = [random.randint(1, 1000) for i in range(VEC_SIZE)]


start = time.time()
for i in range(NUM_RUNS):
    sum(map(lambda x, y: x * y, u, v))
end = time.time()
print(f"{end - start}")
