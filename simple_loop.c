#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


#define VEC_SIZE 1000
#define NUM_LOOPS pow(10, 6)
#define RAND_RANGE 1000


int dot_them(int first_array[], int second_array[], int length) {
    int result = 0;
    for (int i = 0; i < length; i++) {
        result += first_array[i] * second_array[i];
    }
    return result;
}


int main() {

    int u[VEC_SIZE];
    int v[VEC_SIZE];

    srand(time(NULL));

    for (int i = 0; i < VEC_SIZE; i++) {
        u[i] = rand() % RAND_RANGE;
        v[i] = rand() % RAND_RANGE;
    }

    clock_t begin = clock();
    for (int i = 0; i < NUM_LOOPS; i++) {
        dot_them(u, v, VEC_SIZE);
    }
    clock_t end = clock();

    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%f", time_spent);
    return 0;
}
