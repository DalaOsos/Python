from collections import deque


class StackDeque:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def get_head(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


class Stacklst:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Or raise an exception

    def get_head(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    count_elements = 0

    def __init__(self):
        self.head = None

    def printitems(self):
        if self.is_empty():
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        else:
            print('Stack is empty')

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.count_elements += 1

    def pop(self):
        if self.is_empty():
            temp = self.head.data
            self.head = self.head.next
            self.count_elements -= 1
            return temp
        else:
            print('Stack is Empty')

    def is_empty(self):
        return self.head

    def get_head(self):
        if self.is_empty():
            return self.head.data
        else:
            print('Stack is Empty')

    def size(self):
        return self.count_elements


def are_paired(para1, para2):
    if para1 == '(' and para2 == ')':
        return True
    elif para1 == '{' and para2 == '}':
        return True
    elif para1 == '[' and para2 == ']':
        return True
    else:
        return False


def are_balanced(expression):
    stack = Stack()
    for i in expression:
        if i == '(' or i == '[' or i == '{':
            letter = Node(i)
            stack.push(letter)
        elif i == ')' or i == ']' or i == '}':
            if stack.is_empty() and are_paired(stack.get_head(), i):
                stack.pop()
            else:
                return False
    return not stack.is_empty()


def result():
    expression = input('Please enter Expression that you want to check it. ')
    if are_balanced(expression):
        print('Expression is Correct')
    else:
        print('Expression is not correct')
