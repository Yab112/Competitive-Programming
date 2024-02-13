class ListNode:
    def __init__(self, val, key, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  
        self.head = ListNode(0,0,None,None)
        
        self.tail = self.head
        self.hash = {} 
        
    def get(self, key: int) -> int:
        if key in self.hash :
            self.remove(key)
            self.add_(self.hash[key])
            return self.hash[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            temp = ListNode(value,key)
            self.hash[key] = temp
            self.add_(temp)
            
        elif key in self.hash:
            self.hash[key].val = value
            self.remove(self.hash[key].key)
            self.add_(self.hash[key])
        if self.capacity < len(self.hash):
            key = self.head.next.key
            self.remove(key)
            del self.hash[key]
            
    def add_(self,node):
        if node == self.tail:
            return 
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    
    def remove(self,key):
        if self.hash[key] == self.tail:
            return 
        self.hash[key].prev.next = self.hash[key].next
        self.hash[key].next.prev = self.hash[key].prev
        
        
        
        

        
        
            
            
            
        
            
        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)