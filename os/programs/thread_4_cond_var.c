/**
 * source: https://computing.llnl.gov/tutorials/pthreads
 * condition variable example
 * main makes 3 threads. 2 threads update "count" var.
 * the 3rd one waits until "count" var reaches a specified value
 */
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_THREADS 3
#define TCOUNT 10
#define COUNT_LIMIT 12

int count = 0;
int thread_ids[3] = {0, 1, 2};

pthread_mutex_t count_mutex;
pthread_cond_t count_threshold_cv;

void *inc_count(void *t)
{
    int i;
    long my_id = (long)t;

    for (i = 0; i < TCOUNT; i++)
    {
        pthread_mutex_lock(&count_mutex);
        count++;

        // check the value of "count" and signal waiting thread when condition
        // is reached. Note that this occurs while mutex is locked.
        if (count == COUNT_LIMIT)
        {
            // pthread_cond_signal() should be called after mutex is locked
            // and must unlock mutex (see below) in order for 
            // pthread_cond_wait() to complete
            pthread_cond_signal(&count_threshold_cv);
            printf("inc_count(): thread %ld, count = %d threshold reached\n",
                   my_id, count);
        }
        printf("inc_count(): thread %ld, count = %d, unlocking mutex\n", my_id,
               count);
        pthread_mutex_unlock(&count_mutex);

        // do some "work" so threads can alternate on mutex lock
        sleep(1);
    }
    pthread_exit(NULL);
}

void *watch_count(void *t)
{
    long my_id = (long)t;
    printf("starting watch_count(): thread %ld\n", my_id);

    /*
   Lock mutex and wait for signal.  Note that the pthread_cond_wait 
   routine will automatically and atomically unlock mutex while it waits. 
   Also, note that if COUNT_LIMIT is reached before this routine is run by
   the waiting thread, the loop will be skipped to prevent pthread_cond_wait
   from never returning. 
   */
    pthread_mutex_lock(&count_mutex);
    while (count < COUNT_LIMIT)
    {
        // a blocking pthread_cond_wait() call automatically unlocks the associated mutex
        // while it waits.
        // when receiving a signal, wake up, and automatically lock the mutex 
        pthread_cond_wait(&count_threshold_cv, &count_mutex);
        printf("watch_count(): thread %ld condition signal received\n",
            my_id);
    }
    
    count += 125;
    printf("watch_count(): thread %ld count now = %d\n", my_id, count);
    pthread_mutex_unlock(&count_mutex);
    pthread_exit(NULL);
}

int main()
{
    int i, rc;
    long t1 = 1, t2 = 2, t3 = 3;
    pthread_t threads[3];
    pthread_attr_t attr;

    // init mutex and cond var
    pthread_mutex_init(&count_mutex, NULL);
    pthread_cond_init(&count_threshold_cv, NULL);

    // for partability, explicityly create threads in a joinable state
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);
    pthread_create(&threads[0], &attr, watch_count, (void *)t1);
    pthread_create(&threads[1], &attr, inc_count, (void *)t2);
    pthread_create(&threads[2], &attr, inc_count, (void *)t3);

    for (i = 0; i < NUM_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    printf("main(): waitid on %d threads, done\n", NUM_THREADS);

    // clean up and exit
    pthread_attr_destroy(&attr);
    pthread_mutex_destroy(&count_mutex);
    pthread_cond_destroy(&count_threshold_cv);
    pthread_exit(NULL);
}
