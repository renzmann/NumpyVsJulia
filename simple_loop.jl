using LinearAlgebra
using Random
using CSV
using DataFrames
using Printf


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


function calculate_run_times()
    run_data = DataFrame(vec_size = Int[], num_runs=Int[], runtime=Float64[])
    for i=9:9
        for j=0:0
            vec_size = 10^i
            num_runs = 10^j
            @printf("Running combination: `vec_size`=%d ... `num_runs`=%d\r", vec_size, num_runs)
            runtime = many_dot_products(vec_size, num_runs)[2]
            push!(run_data, (vec_size, num_runs, runtime))
        end
    end
    run_data
end


function main()
    run_times = calculate_run_times()
    out_file = "./data/julia_runs.csv"
    @printf("Writing data to %s", out_file)
    CSV.write(out_file, run_times)
end


main()

