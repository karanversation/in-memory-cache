# Author: Karan Bajaj (karanbajaj23@gmail.com)

from copy import deepcopy


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.value)

"""
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, node):
        node.next = deepcopy(self.head)
        self.head = node
        if not self.tail:
            self.tail = node

    def remove_from_back(self):
        node = deepcopy(self.tail)
        self.tail = self.tail.prev
        return node

    def extract_node(self, node):
        if node.prev:
            node.prev.next = deepcopy(node.next)
        if node.next:
            node.next.prev = node.prev
        return node

    def print_list(self):
        node = self.head
        values = []
        while node:
            values.append(str(node))
            node = node.next
        print(' -> '.join(values))

dll = DoublyLinkedList()
dll.add_to_front(Node(10))
dll.add_to_front(Node(20))
dll.print_list()
dll.remove_from_back()
dll.print_list() # fix bug
"""

#### CACHE ####

class Cache:
    def __init__(self, size):
        self.size = size
        self.elements = {}

    def set(self, key, value):
        if len(self.elements) == self.size:
            # need eviction
            print('Cache full')
            pass
        self.elements[key] = value

    def get(self, key):
        return self.elements.get(key)


# Test cases

c = Cache(3)

print(c.get(1))

c.set(1, 100)
print(c.get(1))

c.set(2, 200)
print(c.get(2))

c.set(3, 300)
c.set(4, 400)
