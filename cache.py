# Author: Karan Bajaj (karanbajaj23@gmail.com)

from dll import DoublyLinkedList


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

cache = Cache('lru', 100)

