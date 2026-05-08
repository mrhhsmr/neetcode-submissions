class LRUCache:

    capacity = 0

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.head = Node(-1, -1000000, None, None)
        self.tail = Node(-1, 1000000, None, None)
        self.head.nex = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.del_node(node)
            self.move_tail(node)
            return node.val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            node = self.mp[key]
            node.val = value
            return None
        
        newNode = Node(value, key, None, None)
        self.mp[key] = newNode
        if len(self.mp) > self.capacity:
            headNext = self.head.nex
            self.del_node(headNext)
            del self.mp[headNext.key]
        
        self.move_tail(newNode)

        return None
    
    def del_node(self, node : Node):
        prev = node.prev
        nex = node.nex
        prev.nex = nex 
        nex.prev = prev
    
    def move_tail(self, node : Node):
        tail_prev = self.tail.prev
        tail_prev.nex = node
        node.nex = self.tail
        node.prev = tail_prev
        self.tail.prev = node

        
class Node:
    prev = None
    nex = None
    val = 0
    key = 0

    def __init__(self, val: int, key: int, prev: Node, nex: Node):
        self.val = val
        self.prev = prev
        self.nex = nex
        self.key = key

