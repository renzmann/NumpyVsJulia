import timeit



setup = """
import numpy as np
A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)


def matrix_multiply(a, b):
    return a @ b


def hadamard_multiply(a, b):
    return a * b

"""


if __name__ == '__main__':
    print("Matrix multiplication:")
    num = 500
    time = timeit.timeit("matrix_multiply(A, B)", setup=setup, number=num)
    print(time / num, 's')
    print()
    print("Hadamard multiplication:")
    time = timeit.timeit("hadamard_multiply(A, B)", setup=setup, number=num)
    print(time / num, 's')


