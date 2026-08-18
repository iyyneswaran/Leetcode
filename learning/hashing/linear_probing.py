class HashMapOpenAddressing:
    _EMPTY = object()
    _DELETED = object()

    def __init__(self, capacity = 16):
        self.capacity = capacity
        self.keys = [self._EMPTY] * capacity
        self.values = [None] * capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    
        