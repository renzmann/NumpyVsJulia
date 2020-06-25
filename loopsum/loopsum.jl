using Random
using Printf

try
    using BenchmarkTools
catch
    import Pkg
    Pkg.add("BenchmarkTools")
    Pkg.update("BenchmarkTools")
    using BenchmarkTools
end


function loopsum(n)
    x = 0.
    for i=1:n
        x += rand()
    end
    x
end

o = @benchmark loopsum(n) setup=(n=10^6)
print("Mean time: ", time(o) / 1e6, "ms\n")
