using LinearAlgebra
using Random
using BenchmarkTools


function hadamard_multiply(a, b)
    a .* b
end


function main()
    print("Hadamard multiplication:")
    @benchmark hadamard_multiply(A, B) setup=(A=rand(Float64, (10000, 10000)); B=rand(Float64, (10000, 10000)))
end


main()
