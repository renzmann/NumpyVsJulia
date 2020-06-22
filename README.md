Simple Benchmarking of Python/NumPy Against Julia
=================================================

In this very small repository, we look at a battle of speed between some
very simple programs. In each case, we are taking a dot product of random
integer vectors 1,000,000 times, and measuring the speed at which the loop
completes. There are three implementations so far:

1. Pure python
2. Python + NumPy
3. Pure Julia

I'm testing these on a Windows 10 machine with an Intel i7-7820X
@ 3.60GHz. Results:

1. Python (3.7) : 70.9 s
2. Python (3.7) + NumPy (1.18.1) : 2.23 s
3. Julia (1.4) : 0.49 s

