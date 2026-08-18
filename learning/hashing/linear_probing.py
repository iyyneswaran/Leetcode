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

    def put(self, key, value):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] not in (self._EMPTY, self._DELETED) and self.keys[idx] != key:
            idx = (idx + 1) % self.capacity
            if idx == start:
                raise Exception("Hashmap is full")
        if self.keys[idx] in (self._EMPTY, self._DELETED):
            self.size += 1
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] is not self._EMPTY:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity
            if idx == start:
                break
        raise KeyError(key)

    def remove(self, key):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] is not self._EMPTY:
            if self.keys[idx] == key:
                self.keys[idx] = self._DELETED
                self.values[idx] = None
                self.size -= 1
                return
            idx = (idx + 1) % self.capacity
            if idx == start:
                break
        raise KeyError(key)