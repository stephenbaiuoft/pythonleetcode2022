class Node:
    __slots__ = ['key', 'val', 'prev', 'next']
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        # set up head and tail, and we'd insert in between
        self.head = Node(2022, 2)
        self.tail = Node(2022, 22)
        self.head.next = self.tail
        self.tail.prev = self.head
        # dict for storing key, and node
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if (self.capacity == 0):
            return -1
        
        # non-exist  (return -1)
        if (key not in self.map.keys()):
            return -1
            
        # exist (update order)
        node = self.map[key]
        # if already head, do nothing
        if (node.prev == self.head):
            return node.val
        
        # update order for non-head       
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # bring node to front
        _node = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        _node.prev = node
        node.next = _node
    
        return node.val
        

        

    def put(self, key: int, value: int) -> None:
        if (self.capacity == 0):
            return None
                
        if (key in self.map.keys()):
            found = self.map[key]
            found.val = value
            # update the order 
            self.get(key)
        # not found, we'd need to insert 
        else:
            node = Node(key, value)
            # if full, we'd need to take out and then insert 
            if (len(self.map.keys()) == self.capacity):
                # get rid of the node before tail 
                _node = self.tail.prev
                self.tail.prev = _node.prev
                _node.prev.next = self.tail
                # remove from map
                self.map.pop(_node.key, None)
                
            # we have enough to insert 
            # bring node to front
            _node = self.head.next

            self.head.next = node
            node.prev = self.head

            _node.prev = node
            node.next = _node          
            
            self.map[key] = node
                

lRUCache = LRUCache(2)
lRUCache.put(1, 0)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4,4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)