#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>


#define VEC_SIZE 100000
#define NUM_LOOPS 10000


int dot_them(int first_array[], int second_array[], int length) {
    int result = 0;
    for (int i = 0; i < length; i++) {
        result += first_array[i] * second_array[i];
    }
    return result;
}


int convert_str_to_int(char string[]) {
    int len = strlen(string);
    int result = 0;

    for (int i = 0; i < len; i++) {
        result = result * 10 + (string[i] - '0');
    }

    return result;
}


int main() {
    printf("\nCombination: `vec_size`=%d ... `num_loops`=%d\n\n", VEC_SIZE, NUM_LOOPS);
    int u[NUM_LOOPS];
    int v[VEC_SIZE];

    srand(time(NULL));

    for (int i = 0; i < VEC_SIZE; i++) {
        u[i] = (float)rand() / (float)RAND_MAX;
        v[i] = (float)rand() / (float)RAND_MAX;
    }

    clock_t begin = clock();
    for (int i = 0; i < NUM_LOOPS; i++) {
        dot_them(u, v, VEC_SIZE);
    }
    clock_t end = clock();

    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("\nRuntime=%f\n\n", time_spent);
    return 0;
}
