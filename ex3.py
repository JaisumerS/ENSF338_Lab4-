# Question 1: In the provided code from lists.c, the function responsible for this is list_resize(). This function is 
# called when an element is appended to a list and there's no more room. It calculates the new size for the list, 
# allocates the memory, and copies the old elements to the new memory location.

import time
import sys
import matplotlib.pyplot as plt
import numpy as np

def test_list_growth():
    lst = []
    last_size = 0
    for i in range(64):
        lst.append(i)
        current_size = sys.getsizeof(lst)
        if current_size != last_size:
            print(f"Capacity changed after adding element {i}, new size is {current_size} bytes")
            last_size = current_size

def measure_append_time(S):
    times = []
    for _ in range(1000):
        lst = [0] * S
        start_time = time.perf_counter()
        lst.append(0)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return times

def measure_append_time_minus_1(S):
    times = []
    for _ in range(1000):
        lst = [0] * (S - 1)  # Create a list of size S-1
        start_time = time.perf_counter()
        lst.append(0)  # Append one element to grow the list to size S
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return times


test_list_growth()
S = 568
times = measure_append_time(S)
print(f"Average time to grow the array from size {S} to {S+1}: {sum(times)/len(times)} seconds")
times_minus1 = measure_append_time_minus_1(S)
print(f"Average time to grow the array from size {S-1} to {S}: {sum(times)/len(times)} seconds")

plt.figure(figsize=(10, 6))
plt.hist(times, bins='auto', alpha=0.7, label=f"Size {S} to {S+1}")
plt.hist(times_minus1, bins='auto', alpha=0.7, label=f"Size {S-1} to {S}")
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.title('Distribution of Time to Grow Array')
plt.show()

# Question 5: the distribution for size S to S+1 is slightly skewed to the right, indicating that it generally 
# takes a bit longer to grow the array from size S to S+1 compared to size S-1 to S. This could be due to the fact that 
# growing the array from size S to S+1 might require a reallocation of memory, which takes additional time.
