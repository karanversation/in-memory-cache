# Author: Karan Bajaj (karanbajaj23@gmail.com)


class NotImplementedException(Exception):
    pass

class IEvictionAlgo:
	def get():
		raise NotImplementedException()
	def set():
		raise NotImplementedException()
	def evict(self, cache):
		raise NotImplementedException()


class LRU(IEvictionAlgo):
    def get(self, node, cache):
        pass
    def set(self, node, cache):
        pass
    def evict(self, cache):
        return cache.get_last()

class FIFO(IEvictionAlgo):
    def get(self, node, cache):
        pass
    def set(self, node, cache):
        pass
    def evict(self, cache):
        return cache.get_last()


EVICTION_ALGO_REGISTRY = {
    'lru': LRU,
    'fifo': FIFO
}

class Cache:
    def __init__(self, eviction_algo_str, max_capacity):
        self.map = {} # initialise with max_capacity size
        self.max_capacity = max_capacity
        self.eviction_algo = EVICTION_ALGO_REGISTRY[eviction_algo_str]
        self.dll = DoublyLinkedList()

    def set(self, key, value):
        self.eviction_algo.set(node, self)

    def get(self, key):
        if key not in self.map:
            return None
        node = self.map[key]
        return self.eviction_algo.get(node, self)


class Node:
    def __init__(self, _next=None, prev=None, data=None):
        self._next = _next # reference to _next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node._next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return
        new_node = Node(new_data)
        new_node._next = prev_node._next
        prev_node._next = new_node
        new_node.prev = prev_node
        if new_node._next:
            new_node._next.prev = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last._next:
            last = last._next
        last._next = new_node
        new_node.prev = last
        return

    def printList(self, node):
        print("\nTraversal in forward direction")
        while node:
            print(" {}".format(node.data))
            last = node
            node = node._next
        print("\nTraversal in reverse direction")
        while last:
            print(" {}".format(last.data))
            last = last.prev


cache = Cache('lru', 100)

