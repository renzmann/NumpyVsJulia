using Random
using BenchmarkTools


function loopsum(n)
    x = 0.
    for i=1:n
        x += rand()
    end
    x
end


@benchmark loopsum(n) setup=(n=10^6)
