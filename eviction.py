# Author: Karan Bajaj (karanbajaj23@gmail.com)


class NotImplementedException(Exception):
    pass

class IEvictionAlgo:
    def get(self):
        raise NotImplementedException()
    def set(self):
        raise NotImplementedException()
    def evict(self, cache):
        raise NotImplementedException()
    def __repr__(self):
        return str(self.__class__)


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

