# import threading
# import time
# def task1():
#     print("Task 1")

# def task2():
#     print("Task 2")
#     print("")
# start=time.time()
# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)
# end=time.time()
# t1.start()
# t2.start()

# print(end-start)





'''Normal funtion'''
import time
def fun1():
    print("task 1")
start=time.time()
t1=fun1()
end=time.time()
print(end-start)
print("1 completed")


def fun2():
    print("task 2")
start=time.time()
t2=fun2()
end=time.time()
print("time",end-start)







'''Using Threading'''
import time
import threading
def fun1():
    print("task 1")
def fun2():
    print("task 2")
start = time.time()
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
end = time.time()
print("Total time:", end - start)