from Stack import Node


class LinkedList:
    count_element = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def isempty(self):
        return not self.count_element

    def add_first(self, item):
        node = Node(item)
        if self.count_element == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.count_element += 1

    def add_last(self, item):
        node = Node(item)
        if self.count_element == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count_element += 1

    def add_at_pos(self, item, pos=0):
        node = Node(item)
        if pos < 0 or pos > self.count_element:
            print('Not Possible Because Position Out of Range')
        else:
            if pos == 0:
                self.add_first(item)
            elif pos == self.count_element:
                self.add_last(item)
            else:
                current = self.head
                for i in range(1, pos):
                    current = current.next
                node.next = current.next
                current.next = node
                self.count_element += 1

    def remove_first(self):
        if self.isempty():
            print('The Linked List is empty')
        elif self.count_element == 1:
            temp = self.head
            self.head = self.tail = None
            self.count_element -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.count_element -= 1
            return temp

    def remove_last(self):
        if self.isempty():
            print('The Linked List is empty')
        elif self.count_element == 1:
            temp = self.head
            self.head = self.tail = None
            self.count_element -= 1
            return temp
        else:
            cur = self.head
            pre = self.head.next
            while cur != self.tail:
                pre = cur
                cur = cur.next
            pre.next = None
            self.tail = pre
            self.count_element -= 1
            return cur

    def remove(self, item):
        if self.isempty():
            print('The Linked List is empty')
        elif self.head.data == item:
            self.remove_first()
        else:
            cur = self.head.next
            pre = self.head
            while cur is not None:
                if cur.data == item:
                    break
                pre = cur
                cur = cur.next
            if cur is None:
                print('Not Found')
            else:
                if self.tail == cur:
                    self.remove_last()
                else:
                    pre.next = cur.next
                    self.count_element -= 1

    def reverse(self):
        pre = None
        cur = self.head
        pos = self.head.next

        while pos:
            pos = cur.next
            cur.next = pre
            pre = cur
            cur = pos
        self.tail = self.head
        self.head = pre

    def search(self, element):
        cur = self.head
        pos = 0
        while cur is not None:
            if cur.data == element:
                return pos
            cur = cur.next
            pos += 1
        return -1

    def display_data(self):
        if self.isempty():
            print('The Linked List is Empty')
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
