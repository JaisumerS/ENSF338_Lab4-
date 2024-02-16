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

# Example usage:
if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insertNode(5)
    linkedList.insertNode(3)
    linkedList.insertNode(7)
    linkedList.insertNode(1)

    print("*********************************************************************\n")
    print("The current list is:")
    linkedList.display()
    print()

    print(f'Looking for 3 via binarySearch // Is number in list? - {linkedList.binarySearch(3)}')  
    print(f'Looking for 6 via binarySearch // Is number in list? - {linkedList.binarySearch(6)}')
    print("\n*********************************************************************")   

