# this example shows you how to use multi-threading to let your code run concurrently.

# python multi-threading cannot speed up computation-intensive task.
# but can be use to let tasks with i/o operations to execute concurrently.
import time
import threading

an_important_parameter = "this is really an important parameter that I need to pass into the new thread"

def time_consuming_task(an_important_parameter):
    time.sleep(5)  # sleep for 5 seconds.
    print(an_important_parameter)


# do the task for 5 times.
N_repetition = 5

start1 = time.time()
for i in range(N_repetition):
    time_consuming_task(an_important_parameter)
end1 = time.time()
print("time used for single thread executing:")
print(end1 - start1)


# https://www.tutorialspoint.com/python3/python_multithreading.htm
class MyThread(threading.Thread):
    def __init__(self, an_important_parameter): # let the constructor have parameters.
        self.parameter = an_important_parameter
        threading.Thread.__init__(self)

    def run(self):
        time_consuming_task(self.parameter)


start2 = time.time()
thread_list = list()

for i in range(N_repetition):
    # creating threads.
    t = MyThread(an_important_parameter)
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

