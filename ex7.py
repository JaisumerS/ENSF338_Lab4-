import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_head(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1

    def get_size(self):
        return self.size

    def get_element_at_position(self, pos):
        if pos < 0 or pos >= self.size:
            return None
        current = self.head
        for _ in range(pos):
            current = current.next
        return current.data

# Given Method
def labReverse(self):
    newhead = None
    prevNode = None
    for i in range(self.get_size()-1,-1,-1):
        currNode=self.get_element_at_position(i)
        currNewNode = Node(currNode)
        if newhead is None:
            newhead = currNewNode
        else:
            prevNode.next = currNewNode
        prevNode = currNewNode
    self.head = newhead

# Optimized Method
def optimizedReverse(self):
    if self.head is None or self.head.next is None:
        return
    prevNode = None
    currNode = self.head
    while currNode is not None:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    self.head = prevNode

def create_linked_list(size):
    linked_list = LinkedList()
    for i in range(size):
        linked_list.insert_tail(Node(i))
    return linked_list

def measure_time(func, linked_list):
    start_time = time.time()
    func(linked_list)
    end_time = time.time()
    return end_time - start_time

sizes = [1000, 2000, 3000, 4000]
num_trials = 100

given_times = []
optimized_times = []

for size in sizes:
    linked_list = create_linked_list(size)
    
    given_total_time = 0
    optimized_total_time = 0
    
    for _ in range(num_trials):
        given_total_time += measure_time(labReverse, linked_list)
        optimized_total_time += measure_time(optimizedReverse, linked_list)
    
    given_avg_time = given_total_time / num_trials
    optimized_avg_time = optimized_total_time / num_trials
    
    given_times.append(given_avg_time)
    optimized_times.append(optimized_avg_time)

plt.plot(sizes, given_times, label='Given Method')
plt.plot(sizes, optimized_times, label='Optimized Method')
plt.xlabel('List Size')
plt.ylabel('Average Time (s)')
plt.title('Comparison of Reversal Methods')
plt.legend()
plt.show()
