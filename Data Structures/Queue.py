from Stack import Node
from collections import deque


class QueueLL:
    count_elements = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def isempty(self):
        return not self.count_element

    def enqueue(self, item):
        node = Node(item)
        if self.isempty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count_elements += 1

    def dequeqe(self):
        if self.isempty():
            print('The Queue is Empty')
        elif self.count_elements == 1:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.count_elements -= 1
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            self.count_elements -= 1
            return temp

    def get_head(self):
        if not self.isempty():
            return self.head.data

    def get_tail(self):
        if not self.isempty():
            return self.tail.data

    def get_size(self):
        return self.count_elements

    def display_data(self):
        if self.isempty():
            print('The Queue is Empty')
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

    def clear(self):
        self.head = None
        self.tail = None
        self.count_elements = 0


class QueueDE:

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return None  # Or raise an exception

    def get_head(self):
        return self.items[0]

    def get_tail(self):
        return self.items[-1]

    def get_size(self):
        return len(self.items)

    def display_data(self):
        for i in self.items:
            print(i)

    def clear(self):
        self.items.clear()


class ListQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def get_head(self):
        return self.items[0]

    def get_tail(self):
        return self.items[-1]

    def get_size(self):
        return len(self.items)

    def display_data(self):
        for i in self.items:
            print(i)

    def clear(self):
        self.items.clear()
