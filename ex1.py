import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

# Question 4 Response:
# The complexity for linked list binary search is O(nlogn).
# The reason being, is that for each step of the binary search, getting a list 'index'
# is an operation where you traverse from the head of the list to the spot it needs, requiring
# O(n) linear time. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print("None")

    def to_sorted_list(self):
        sorted_list = []
        current_node = self.head
        while current_node:
            sorted_list.append(current_node.data)
            current_node = current_node.next
        sorted_list.sort()
        return sorted_list

    def binarySearch(self, num):
        sorted_list = self.to_sorted_list()
        left, right = 0, len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid] == num:
                return True
            elif sorted_list[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
class IntArray:
    def __init__(self):
        self.array = []

    def append(self, value):
        self.array.append(value)

    def display(self):
        print("Array contents: ", end="")
        for value in self.array:
            print(value, end=" ")
        print()

    def binarySearch(self, target):
        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1  # Indicates target not found


def binaryList(linked_list, target):
    return linked_list.binarySearch(target)

def binaryArray(array, target):
    return array.binarySearch(target)

def plotMe(input_sizes, array_search_times, linked_list_search_times):
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, array_search_times, label='Array Binary Search', marker='o')
    plt.plot(input_sizes, linked_list_search_times, label='Linked List Binary Search', marker='o')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Performance of Binary Search in Array vs Linked List')
    plt.legend()
    plt.grid(True)
    plt.show()


# Algorithims
if __name__ == "__main__":
    #LinkedList
    linkedList = LinkedList()
    linkedList.insertNode(5)
    linkedList.insertNode(3)
    linkedList.insertNode(7)
    linkedList.insertNode(1)

    print("*********************************************************************\n")
    print("The current list is:")
    linkedList.display()
    print()

    print(f'Looking for 3 via binarySearch // Is number in linked list? - {linkedList.binarySearch(3)}')  
    print(f'Looking for 6 via binarySearch // Is number in linked list? - {linkedList.binarySearch(6)}')
    print("\n*********************************************************************\n")   

    #Array
    arr = IntArray()
    arr.append(1)
    arr.append(3)
    arr.append(5)
    arr.append(7)
    arr.append(9)

    target = 5
    index = arr.binarySearch(target)
    arr.display()
    print("\nConducting Binary Search:")
    if index != -1:
        print(f"Found {target} at index {index}.")
    else:
        print(f"{target} not found.")
    
    print("\n*********************************************************************\n")
    print("Timing for Q5:")

    input_sizes = [1000, 2000, 4000, 8000]
    num_trials = 100

    arrayTimes = []
    linkedTimes = []

    for size in input_sizes:
        array = [random.randint(0, size * 10) for _ in range(size)]
        array.sort()  
        linked_list = LinkedList()
        for num in array:
            linked_list.prepend(num)
        arrayTest = IntArray()
        arrayTest.append(random.randint(0, size * 10))
        arrayTest.array.sort()

        arrayTime = timeit.timeit(lambda: binaryArray(arrayTest, random.randint(0, size * 10)), number=num_trials) / num_trials
        linkedTime = timeit.timeit(lambda: binaryList(linked_list, random.randint(0, size * 10)), number=num_trials) / num_trials

        arrayTimes.append(arrayTime)
        linkedTimes.append(linkedTime)

        print(f"Input Size: {size}")
        print(f"Array Binary Search Average Time: {arrayTime:.6f} seconds")
        print(f"Linked List Binary Search Average Time: {linkedTime:.6f} seconds")
        print()  

        print("\n*********************************************************************")

    plotMe(input_sizes, arrayTimes, linkedTimes)

