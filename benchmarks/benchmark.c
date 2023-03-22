// There is virtually no difference between looping over the array to find the min, or calling
// min() multiple times

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int min(int a, int b)
{
    return (a > b) ? b : a;
}

int min_int(int arr[], size_t size)
{
    // simply loop over an array of integers to find the min
    int min = arr[0];
    for (size_t i = 1; i < size; i++)
    {
        int val = arr[i];
        if (val < min)
        {
            min = val;
        }
    }
    
    return min;
}

void time_func(void (*f)(), int iterations, int warmups)
{
    for (size_t i = 0; i < warmups; i++)
    {
        (*f)();
    }
    
    float total_runtime;
    for (size_t i = 0; i < iterations; i++)
    {
        float start = (float)clock() / CLOCKS_PER_SEC;
        (*f)();
        float end = (float)clock() / CLOCKS_PER_SEC;

        total_runtime += (end - start);
    }

    float avg_runtime = total_runtime / iterations;
    printf("Ran for %.6f seconds, avg of %.6f", total_runtime, avg_runtime);
}

void min_int_time()
{
    int arr[4] = { 1, 2, 3, 4 };
    min_int(arr, 4);
}

void min_time()
{
    min(min(1, 2), min(3, 4));
}

int main()
{
    time_func(min_int_time, 100000, 10);
    printf("\n");
    time_func(min_time, 100000, 10);
}