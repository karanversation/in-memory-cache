# Author: Karan Bajaj (karanbajaj23@gmail.com)

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next - None

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

c = Cache(3)

print(c.get(1))

c.set(1, 100)
print(c.get(1))

c.set(2, 200)
print(c.get(2))

c.set(3, 300)
c.set(4, 400)
