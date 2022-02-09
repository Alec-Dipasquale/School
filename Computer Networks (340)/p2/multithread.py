# this example shows you how to use multi-threading to let your code run concurrently.

# python multi-threading cannot speed up computation-intensive task.
# but can be use to let tasks with i/o operations to execute concurrently.
import time
import threading


def time_consuming_task():
    time.sleep(5)  # sleep for 5 seconds.


# do the task for 5 times.
N_repetition = 5

start1 = time.time()
for i in range(N_repetition):
    time_consuming_task()
end1 = time.time()
print("time used for single thread executing:")
print(end1 - start1)


# https://www.tutorialspoint.com/python3/python_multithreading.htm
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time_consuming_task()


start2 = time.time()
thread_list = list()

for i in range(N_repetition):
    # creating threads.
    t = MyThread()
    thread_list.append(t)

for t in thread_list:
    # starting & running threads.
    t.start()

for t in thread_list:
    # waiting for all threads to finish
    t.join()

end2 = time.time()
print("time used for multi-threaded executing:")
print(end2 - start2)

