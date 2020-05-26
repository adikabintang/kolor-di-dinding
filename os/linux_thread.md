Sources: 

- https://computing.llnl.gov/tutorials/pthreads/
- http://outofsync.net/wiki/index.php?title=Monitoring_linux_system_performance
- https://stackoverflow.com/questions/20772476/when-to-use-pthread-condition-variables
- https://en.wikipedia.org/wiki/Priority_inversion

# Process vs Thread

![proc](https://computing.llnl.gov/tutorials/pthreads/images/process.gif)

![thread](https://computing.llnl.gov/tutorials/pthreads/images/thread.gif)

Images source: https://computing.llnl.gov/tutorials/pthreads/

Main difference: thread only has its own stack. The rest is the same. This implies:

1. A thread is lighter than a process
2. Other than stack region, such as heap and file mapping, are shared between process and threads
3. Spawning a thread is less expensive than spawning a new process because a thread does not need to copy resources on creation
4. Kernel assigns 

![creating_proc_vs_thread](http://outofsync.net/wiki/images/1/15/Process_thread.gif)

image source: http://outofsync.net/wiki/index.php?title=Monitoring_linux_system_performance



# Models for threaded programs:

1. Manager-worker: manager takes input, assign work to workers. The workers can be in form of a thread pool.
2. Pipeline: a task is broken down into pieces, each piece is done by a thread.
3. Peer: like manager-worker but the manager works too.

# Mutex

- Mutex is used to synchronize threads and to protect shared data when multiple writes occur.
- This prevents a **race condition**.
- Usually it is used to update a global variable
- The variable that is accessed/written by multiple threads are called "critical section".
- Flow of the use of mutex:
  - Create and initialize a mutex variable
  - Several threads attempt to lock the mutex
  - Only one thread got it, the others which fail are blocked, waiting it to be released
  - The mutex owner does some action, then unlock the mutex
  - Another thread get the mutex and repeat the process
  - finally, the mutex is destroyed
- Mutex attribute in pthread provides some ways to prevent priority inversions for a mutex. Priority inversion is when the higher priority is preempted by a lower priority.
- If multiple threads is waiting for a locked mutex, after the mutex is released, the next thread that will be granted the mutex appears to be random.
- `pthread_mutex_lock` blocks. We can use `pthread_mutex_trylock()` to attempt to lock a mutex (and does not block/return a busy error code when it is already locked by another thread). This may be useful in preventing deadlocks.

# Condition variable

1. Difference between mutex and condition variable:
   1. Mutex implement synchronization by controlling thread access to data
   2. Condition variable implement synchronization based on the actual value of data

Typical usage of condition variable:

**Task 1**: Done by thread A, does something then signals B who are running another task (A telling B to go ahead. B waits until it is signalled by A)

```C
// there is a global variable "bool done = false;"
pthread_mutex_lock(&lock);
// do something
done = true;
pthread_cond_signal(&cond);
pthread_mutex_unlock(&lock);
```

**Task 2**: Done by thread B

```C
pthread_mutex_lock(&lock);
while (!done) { // can also be a counter. the point is it waits when this condition == false
  pthread_cond_wait(&cond);
}
// do something
pthread_mutex_unlock(&lock);
```

In the above example, the result is task A is done before task B.

# Misc

1. When saying "thread-safe", it generally means "no race condition".
2. Priority inversion example:
   1. 3 tasks with different priority, implied by the names: LOW, MEDIUM, HIGH
   2. LOW and HIGH depends on a resource R
   3. LOW accesses the R
   4. HIGH wants to access the R. LOW must release R immediately because HIGH has higher priority
   5. MEDIUM wants to do something, causing LOW to stop working before it releases R
   6. HIGH gets blocked
   7. Although it can cause delay to the overall process (unlike deadlock that makes the whole task wait indefinitely), it can be ignored sometimes.