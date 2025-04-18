class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def delete_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def move_to_head(self, node):
        self.delete_node(node)
        self.add_node(node)

    def pop_tail(self):
        res = self.tail.prev
        self.delete_node(res)
        return res

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            return
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add_node(new_node)
        if len(self.cache) > self.capacity:
            lru = self.pop_tail()
            del self.cache[lru.key]


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))