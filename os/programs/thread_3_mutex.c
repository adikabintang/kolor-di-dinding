/**
 * source: https://computing.llnl.gov/tutorials/pthreads
 * - This is an example of how to use mutex in a program that performs
 * a dot product. 
 * - The shared data is the global struct.
 * - Each thread works on different part of the data
 */
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 4
#define VEC_LEN 100

typedef struct 
{
    double *a;
    double *b;
    double sum;
    int veclen;
} dotdata;

dotdata dotstr;
pthread_t call_thread[NUM_THREADS];
pthread_mutex_t mutexsum;

// see this pattern:
// in a single threaded program, we pass the struct object as a pointer
// to a function, like void *dotprod(struct *val). But in a multithreaded,
// typically the argument is only the thread number and all other information
// is accessed from the globally accessible structure.
void *dotprod(void *arg)
{
    int i, start, end, len;
    long offset;
    double mysum, *x, *y;
    offset = (long)arg;

    len = dotstr.veclen;
    start = offset * len;
    end = start + len;
    x = dotstr.a;
    y = dotstr.b;

    mysum = 0;
    for (i = start; i < end; i++)
    {
        mysum += (x[i] * y[i]);
    }

    // lock a mutex prior to writing/updating shared var,
    // and unlock it
    pthread_mutex_lock(&mutexsum);
    dotstr.sum += mysum;
    pthread_mutex_unlock(&mutexsum);

    pthread_exit((void *) 0);
}

int main()
{
    long i;
    double *a, *b;
    void *status;
    pthread_attr_t attr;

    a = (double *) malloc(NUM_THREADS * VEC_LEN * sizeof(double));
    b = (double *) malloc(NUM_THREADS * VEC_LEN * sizeof(double));

    for (i = 0; i < VEC_LEN * NUM_THREADS; i++)
    {
        a[i] = 1.0;
        b[i] = a[i];
    }

    dotstr.veclen = VEC_LEN;
    dotstr.a = a;
    dotstr.b = b;
    dotstr.sum = 0;

    // mutex is init by main/spawner of the thread
    pthread_mutex_init(&mutexsum, NULL);

    // set a joinable thread
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    for (i = 0; i < NUM_THREADS; i++)
    {
        pthread_create(&call_thread[i], &attr, dotprod, (void *)i);
    }

    pthread_attr_destroy(&attr);

    // wait on the other threads
    for (i = 0; i < NUM_THREADS; i++)
    {
        pthread_join(call_thread[i], &status);
    }

    printf("sum = %f\n", dotstr.sum);
    free(a);
    free(b);
    pthread_mutex_destroy(&mutexsum);
    pthread_exit(NULL);
}
