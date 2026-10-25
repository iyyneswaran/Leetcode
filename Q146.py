class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()   
        self.left.next = self.right
        self.right.prev = self.left    

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None 

    def _insert_mru(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:        
            node = self.cache[key]
            self._remove(node)
            self._insert_mru(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_mru(node)
            return 

        if len(self.cache) >= self.capacity:
            lru_node = self.left.next
            self._remove(lru_node)
            del self.cache[lru_node.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_mru(new_node)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)