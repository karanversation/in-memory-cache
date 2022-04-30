# Author: Karan Bajaj (karanbajaj23@gmail.com)


class Node:
    def __init__(self, _next=None, prev=None, data=None):
        self._next = _next # reference to _next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = data

    def __repr__(self):
        return 'Node(data={})'.format(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node._next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("previous node cannot be NULL")
            return
        new_node = Node(data=new_data)
        new_node._next = prev_node._next
        prev_node._next = new_node
        new_node.prev = prev_node
        if new_node._next:
            new_node._next.prev = new_node

    def append(self, new_data):
        new_node = Node(data=new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last._next:
            last = last._next
        last._next = new_node
        new_node.prev = last
        return

    def printList(self, node=None):
        node = node or self.head
        print("Traversal in forward direction")
        while node:
            print(" {}".format(node.data))
            last = node
            node = node._next
        print("Traversal in reverse direction")
        while last:
            print(" {}".format(last.data))
            last = last.prev

    def __repr__(self):
        return 'DoublyLinkedList(head={})'.format(self.head)

