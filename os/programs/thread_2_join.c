/**
 * source: https://computing.llnl.gov/tutorials/pthreads/
 */
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM_THREADS 4

void *busy_work(void *t)
{
    int i;
    long tid;
    double result = 0.0;
    tid = (long)t;
    printf("thread %ld starting ...\n", tid);
    for (i = 0; i < 1000000; i++)
    {
        result = result + sin(i) * tan(i);
    }
    printf("thread %ld done. result: %e\n", tid, result);
    pthread_exit((void *)t);
}

int main()
{
    pthread_t thread[NUM_THREADS];
    pthread_attr_t attr;
    int rc;
    long t;
    void *status;

    // initialize and set thread detached attribute to make it joinable explicitly
    // actually this is not always needed. but to make it portable, just do it.
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    for (t = 0; t < NUM_THREADS; t++)
    {
        printf("main: creating thread %ld\n", t);
        rc = pthread_create(&thread[t], &attr, busy_work, (void *)t);
        if (rc)
        {
            printf("error: return code %d\n", rc);
            exit(-1);
        }
    }

    // free attribute
    pthread_attr_destroy(&attr);

    // wait for other threads
    for (t = 0; t < NUM_THREADS; t++)
    {
        rc = pthread_join(thread[t], &status);
        if (rc)
        {
            printf("error: %d\n", rc);
            exit(-1);
        }
        printf("main: completed join with thread %ld having a status\
            of %ld\n",
               t, (long)status);
    }

    printf("Main: program completed. Exiting.\n");
    pthread_exit(NULL);
}