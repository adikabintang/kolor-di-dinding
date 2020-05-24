/**
 * https://leetcode.com/problems/print-in-order
 * Runtime: 108 ms, faster than 89.89% of C online submissions 
 * Memory Usage: 6.3 MB, less than 100.00% of C online submissions
 */
typedef struct {
    // User defined data may be declared here.
    bool first_done, second_done;
    pthread_mutex_t mutex;
    pthread_cond_t first_cond_var, second_cond_var;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    
    // Initialize user defined data here.
    obj->first_done = false;
    obj->second_done = false;
    pthread_mutex_init(&(obj->mutex), NULL);
    pthread_cond_init(&(obj->first_cond_var), NULL);
    pthread_cond_init(&(obj->second_cond_var), NULL);
    
    return obj;
}

void first(Foo* obj) {
    pthread_mutex_lock(&(obj->mutex));
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    obj->first_done = true;
    pthread_cond_signal(&(obj->first_cond_var));
    pthread_mutex_unlock(&(obj->mutex));
}

void second(Foo* obj) {
    pthread_mutex_lock(&(obj->mutex));
    while (!obj->first_done) {
        pthread_cond_wait(&(obj->first_cond_var), &(obj->mutex));
    }
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    obj->second_done = true;
    pthread_cond_signal(&(obj->second_cond_var));
    pthread_mutex_unlock(&(obj->mutex));
}

void third(Foo* obj) {
    pthread_mutex_lock(&(obj->mutex));
    while (!obj->second_done) {
        pthread_cond_wait(&(obj->second_cond_var), &(obj->mutex));
    }
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
    pthread_mutex_unlock(&(obj->mutex));
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    pthread_mutex_destroy(&(obj->mutex));
    pthread_cond_destroy(&(obj->second_cond_var));
    pthread_cond_destroy(&(obj->first_cond_var));
}
