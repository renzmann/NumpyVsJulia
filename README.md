Simple Benchmarking of Python/NumPy Against Julia
=================================================

The test results below were run on a moderately powered Windows 10 surface
pro with an Intel i7-8650U @ 1.90GHz and 16GB RAM. Other machines I've
tried had results come out similarly proportioned to one another, although
the actual runtimes would vary. To replicate these tests yourself, you
will need:

1. Python 3.7, with `numpy` version 1.18 (`pip install numpy==1.18`)
1. Julia 1.4
1. A way to compile C


Repeated dot products
---------------------

In this very small repository, we look at a battle of speed between some
very simple programs. In each case, we are taking a dot product of two
vectors, each consisting of 10,000 random float64 values between 0 and 1,
1,000,000 times, and measuring the speed at which the loop completes.

1. Python (3.7) : 116.5 s
1. Python (3.7) + NumPy (1.18.1) : 5.64 s
1. Julia (1.4) : 2.43 s


Loopsum implementation benchmarks
---------------------------------

The above was looking at how well the underlying BLAS implementation
works, but not necessarily the strength of the language implementation
itself. In the ``loopsum`` examples, we take a look at another short
program and how it performs on each platform. This program clocks the
amount of time it takes to generate 1,000,000 random float values in [0,
1], and take their sum:

1. Python (3.7) 146 ms ± 17.9 ms
1. Python (3.7) + NumPy (1.18.4) 16 ms ± 1.15 ms
1. Julia (1.4) 8.98 ms ± 5 ms
1. C (compiled with gcc in MinGW64) 17.43 ms ± 6.12 ms

