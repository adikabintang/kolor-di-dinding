/**
 * https://computing.llnl.gov/tutorials/pthreads/
 */
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 5

void *print_hello(void *thread_id)
{
    long tid = (long)thread_id;
    printf("hello, this is thread %ld\n", tid);
    pthread_exit(NULL);
}

int main()
{
    pthread_t threads[NUM_THREADS];
    int rc;
    long t;
    for (t = 0; t < NUM_THREADS; t++)
    {
        printf("In main: creating thread %ld\n", t);
        rc = pthread_create(&threads[t], NULL, print_hello, (void *)t);
        if (rc)
        {
            printf("errorL return codeL %d\n", rc);
            exit(-1);
        }
    }

    // By having main() explicitly call pthread_exit() as the last thing 
    //it does, main() will block and kept alive to support the threads it 
    // created until they are done.
    pthread_exit(NULL);
}
