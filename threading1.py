import threading
import time
import concurrent.futures #May use this to replace threading module
from time import perf_counter

start = time.perf_counter() #Counting performance

def do_something(seconds):
    print(f"Sleeping {seconds} second")
    time.sleep(seconds)
    #print("Done sleeping")
    return f'Done sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:

    secs = [5, 4, 3, 2, 1]

    results = executor.map(do_something, secs)

    for result in results:
        print(result)
    # #Understand the list comprehension for 2D matrix as well
    # results = [executor.submit(do_something, sec) for sec in secs]
    
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    
    #Submit methods schedule a function to be executed in n seconds
    #and return a future object
    
    #f = executor.submit(do_something, 1) #submit = start + join in old-school approach
   
    #print(f.result()) #Run the return value of the thread
  

#Create the threads, set target to do_something function but not to execute
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# #Start the thread

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# threads = []

# #For 10 threads running concurrently, the time it take would also probably be 1
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t) #Append the threads that started
#     #Note: putting t.join() here is just equivalent to having 10 threads run 
#     #simultaneously. Instead, create list of threads, then join later

# for thread in threads:
#     thread.join()

     
#do_something()
finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')
