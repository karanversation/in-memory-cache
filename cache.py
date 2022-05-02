# Author: Karan Bajaj (karanbajaj23@gmail.com)

import dll
import eviction

class Cache:
    def __init__(self, eviction_algo_str, max_capacity):
        self.map = {} # initialise with max_capacity size
        self.max_capacity = max_capacity
        self.eviction_algo = eviction.EVICTION_ALGO_REGISTRY[eviction_algo_str]
        self.dll = dll.DoublyLinkedList()

    def set(self, key, value):
        self.eviction_algo.set(node, self)

    def get(self, key):
        if key not in self.map:
            return None
        node = self.map[key]
        return self.eviction_algo.get(node, self)

    def __repr__(self):
        return 'Cache(eviction_algo={})'.format(self.eviction_algo)


cache = Cache('lru', 100)

