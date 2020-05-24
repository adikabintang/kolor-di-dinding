/**
 * https://leetcode.com/problems/print-in-order/
 * https://stackoverflow.com/questions/20772476/when-to-use-pthread-condition-variables
 */
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdbool.h>

pthread_mutex_t mutex;
pthread_cond_t cond_var;
bool first_done = false, second_done = false;

void *first(void *thread_id) {
    pthread_mutex_lock(&mutex);
    printf("first ");
    first_done = true;
    pthread_cond_signal(&cond_var);
    pthread_mutex_unlock(&mutex);
    pthread_exit(NULL);
}

void *second(void *thread_id) {
    pthread_mutex_lock(&mutex);
    // a blocking pthread_cond_wait() call automatically unlocks the associated mutex
    // while it waits.
    // when receiving a signal, wake up, and automatically lock the mutex
    while (!first_done) {
        pthread_cond_wait(&cond_var, &mutex);
    }
    
    printf("second ");
    second_done = true;
    pthread_cond_signal(&cond_var);
    pthread_mutex_unlock(&mutex);
    pthread_exit(NULL);
}

void *third(void *thread_id) {
    pthread_mutex_lock(&mutex);
    while (!second_done) {
        pthread_cond_wait(&cond_var, &mutex);
    }
    printf("third ");
    pthread_mutex_unlock(&mutex);
    pthread_exit(NULL);
}

int main() {
    pthread_t a, b, c;
    pthread_attr_t attr;

    // init mutex and cond var
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&cond_var, NULL);
    //pthread_cond_init(&second_done_cv, NULL);
    
    // set as joinable
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    if (pthread_create(&c, NULL, third, NULL) ||
        pthread_create(&a, NULL, first, NULL) ||
        pthread_create(&b, NULL, second, NULL)) {
        
        perror("failed to create threads\n");
        exit(-1);
    }

    pthread_join(a, NULL);
    pthread_join(b, NULL);
    pthread_join(c, NULL);

    // clean up
    pthread_attr_destroy(&attr);
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond_var);
    
    return 0;
}
