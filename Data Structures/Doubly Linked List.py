class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    count_element = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def isempty(self):
        return not self.count_element

    def add_first(self, item):
        node = Node(item)
        if self.isempty():
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.count_element += 1

    def add_last(self, item):
        node = Node(item)
        if self.isempty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count_element += 1

    def add_at_pos(self, item, pos):
        node = Node(item)
        if pos < 0 or pos > self.count_element:
            print('Not Possible Because Position Out of Range')
        else:
            if pos == 0:
                self.add_first(item)
            elif pos == self.count_element:
                self.add_last(item)
            else:
                cur = self.head
                for i in range(1, pos):
                    cur = cur.next
                node.next = cur.next
                node.prev = cur
                cur.next = node
                cur.next.prev = node

    def remove_first(self):
        if self.isempty():
            print('The Linked List is Empty')
        elif self.count_element == 1:
            self.head = self.tail = None
            self.count_element -= 1
        else:
            self.head = self.head.next
            self.head.prev = None
            self.count_element -= 1

    def remove_last(self):
        if self.isempty():
            print('The Linked List is Empty')
        elif self.count_element == 1:
            self.head = self.tail = None
            self.count_element -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.count_element -= 1

    def remove_at_pos(self, item):
        if self.isempty():
            print('The Linked List is Empty')
        elif self.head.data == item:
            self.remove_first()
        else:
            cur = self.head.next
            while cur is not None:
                if cur.data == item:
                    break
                cur = cur.next
            if cur is None:
                print('Item is Not Found')
            elif cur.next is None:
                self.remove_last()
            else:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                self.count_element -= 1

    def display_data(self):
        if self.isempty():
            print('The Linked List is Empty')
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

    def display_data_reversed(self):
        if self.isempty():
            print('The Linked List is Empty')
        else:
            temp = self.tail
            while temp:
                print(temp.data)
                temp = temp.prev
