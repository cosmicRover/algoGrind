import collections

class LRUCache:
    '''
    index 0 -> back
    index -1 -> front
    
    when using an ordered dict solution, make sure to mention how ordered dict behaves
    just like a doubly linked list with pointers on head and tail of the list
    
    time O(1) | space O(cap)
    
    '''

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.cap = capacity
        self.count = 0
        
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        val = self.dic[key]
        self.dic.move_to_end(key) #move_to_end reorders the element as the [-1] item O(1)
        return val
        
    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            self.count += 1
            
        self.dic[key] = value
        
        if self.count > self.cap:
            self.dic.popitem(last = False) #O(1) time pops the item on first index
            self.count -= 1
            
        self.dic.move_to_end(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)