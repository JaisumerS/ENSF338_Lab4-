
import time
import matplotlib.pyplot as plt
import numpy as np
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2
                
#Question 1: The best case scenario for this function is O(n) when li[i] is less than or equal to 5. In this case,
# the function will only iterate through the list once and perform a constant number of operations on each element.
# The worst case scenario is O(n^2) when li[i] is greater than 5. In this case, the function will iterate through the
# list once and then iterate through the list again for each element greater than 5
# The average case scenario is O(n^2)
#Question 2: The average, best and worst case is not the same
def processdatafixed(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2
# The worst , best, average case is now O(n)

#Question 3:
# Inefficient code
def linearsearch(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1
# Worst case: O(n)
#Efficient code
def binarysearch(li, target):
    left, right = 0, len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == target:
            return mid
        elif li[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#Worst case: O(log n)

def measure_time(func, input_data, target):
    start_time = time.perf_counter()
    func(input_data, target)
    end_time = time.perf_counter()
    return end_time - start_time
def run_experiment():
    # Generate large inputs
    input_data = sorted([np.random.randint(1, 10000) for _ in range(1000)])
    target = np.random.randint(1, 10000)

    # Measure execution time for both functions
    times_linearsearch = [measure_time(linearsearch, input_data, target) for _ in range(100)]
    times_binarysearch = [measure_time(binarysearch, input_data, target) for _ in range(100)]

    # Plot the distribution of measured values
    plt.figure(figsize=(10, 6))
    plt.plot(times_linearsearch, label='linearsearch')
    plt.plot(times_binarysearch, label='binarysearch')
    plt.xlabel('Measurement')
    plt.ylabel('Time (seconds)')
    plt.legend(loc='upper right')
    plt.title('Execution Time of Linear Search vs Binary Search')
    plt.show()

run_experiment()