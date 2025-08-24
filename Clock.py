import time

print("Name, Age:", end=" ")
start_time = time.perf_counter()   
inf = input()                      
timetaken = time.perf_counter() - start_time
print("Time taken is", timetaken, "secs")
