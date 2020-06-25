using LinearAlgebra
using Random
using BenchmarkTools


function matrix_multiply(a, b)
    a * b
end


function time_multiply()
    print("Matrix multiplication:")
    @benchmark matrix_multiply(A, B) setup=(A=rand(Float64, (10000, 10000)); B=rand(Float64, (10000, 10000)))
end


time_multiply()
