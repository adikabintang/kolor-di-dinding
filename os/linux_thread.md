Source: https://computing.llnl.gov/tutorials/pthreads/

# Process vs Thread

![proc](https://computing.llnl.gov/tutorials/pthreads/images/process.gif)

![thread](https://computing.llnl.gov/tutorials/pthreads/images/thread.gif)

Images source: https://computing.llnl.gov/tutorials/pthreads/

Main difference: thread only has its own stack. The rest is the same. This implies:

1. A thread is lighter than a process
2. Other than stack region, such as heap and file mapping, are shared between process and threads.

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
   1. Mutext implement synchronization by controlling thread access to data
   2. Condition variable implement synchronization based on the actual value of data
2. 


# Misc

1. When saying "thread-safe", it generally means "no race condition".
2. 