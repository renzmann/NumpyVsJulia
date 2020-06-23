#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define NUM_LOOPS (int) pow(10, 6)
#define NUM_EVALS (int) 1000

float run_sum(int n) {

    float runningsum = 0.0;

    for (int i = 0.0; i < n; i++) {
        runningsum += rand();
    }

    return runningsum;
}


float timedrun(int n) {
    float total;
    clock_t begin = clock();
    total = run_sum(n);
    clock_t end = clock();
    return (float)(end - begin) / CLOCKS_PER_SEC;
}


int main() {

    float total_time = 0.0;
    float runtimes[NUM_EVALS];
    srand(time(NULL));

    for (int i=0; i < NUM_EVALS; i++) {
        runtimes[i] = timedrun(NUM_LOOPS);
        total_time += runtimes[i];
    }

    float meantime = total_time / NUM_EVALS;
    float sum_squares = 0.0;
    for (int i=0; i < NUM_EVALS; i++) {
        sum_squares += pow(runtimes[i] - meantime, 2);
    }

    float std = sqrt(sum_squares / NUM_EVALS);

    printf("mean runtime: %f ms (+/- %f ms)", meantime * 1000, std * 1000);

    return 0;
}
