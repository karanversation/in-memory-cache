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

