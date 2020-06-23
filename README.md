Simple Benchmarking of Python/NumPy Against Julia
=================================================

In this very small repository, we look at a battle of speed between some
very simple programs. In each case, we are taking a dot product of two
10,000-dimensional random float64 vectors 1,000,000 times, and measuring
the speed at which the loop completes. There are three implementations so
far:

1. Pure python
2. Python + NumPy
3. Pure Julia

I'm testing these on a Windows 10 machine with an Intel i7-7820X
@ 3.60GHz. Results:

1. Python (3.7) : 61.6 s
2. Python (3.7) + NumPy (1.18.1) : 3.19 s
3. Julia (1.4) : 1.04 s


Loopsum implementation benchmarks
---------------------------------

The above was looking at one particular

1. Python (3.7) 146 ms ± 17.9 ms
1. Julia (1.4) 8.98 ms ± 5 ms
1. C (compiled with gcc in MinGW 64 bit) 17.43 ms ± 6.12 ms

