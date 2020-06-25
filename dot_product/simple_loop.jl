using Random
using LinearAlgebra


function dot_them(u, v, num_runs)
    for i=1:num_runs
        dot(u, v)
    end
end


function many_dot_products(vec_size=10^4, num_runs=10^6)
    u = rand(vec_size)
    v = rand(vec_size)
    @timed dot_them(u, v, num_runs)
end


function main()
    run_time = many_dot_products()[2]
    print(run_time)
end


main()
