using LinearAlgebra
using Random


function dot_them(u, v, num_runs)
    for i=1:num_runs
        dot(u, v)
    end
end


function many_dot_products(num_runs=10^6, vec_size=1000)
    u = rand((1:1000), vec_size)
    v = rand((1:1000), vec_size)
    @time dot_them(u, v, num_runs)
end


many_dot_products()
many_dot_products()
