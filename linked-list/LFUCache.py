#*****This problem needs further work******


class Node:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.maxFreq = 1
        self.counter = 0

        self.head = Node(0, 0, -99)
        self.tail = Node(0, 0, -99)

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        #also increment frequency
        if key not in self.dic.keys(): return -1

        #get node from key. Inc the freq and remove it's links
        dicNode = self.dic[key]
        dicNode.freq += 1
        self.maxFreq = max(self.maxFreq, dicNode.freq)
        self._remove(dicNode)
        self._add(dicNode)
        
        return self.dic[key].value


    def put(self, key: int, value: int) -> None:
        
        if key not in self.dic.keys():
            node = Node(key, value, 1)
            self._add(node)
            self.dic[key] = node
            self.counter += 1
        
        #if key exists 
        # update value 
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            
            node.value = value
            node.freq += 1
            self.maxFreq = max(self.maxFreq, node.freq)
            
            self._add(node)
            self.dic[key].value = node.value

        # if key don't exist
        if self.counter > self.capacity:
            nodeToEvict:Node
            minFreq = float("inf")
            sameFreqEncountered = 1
            
            for key in self.dic.keys():
                if self.dic[key].freq == self.maxFreq:
                    sameFreqEncountered += 1
                    
            if sameFreqEncountered == self.capacity:
                del self.dic[self.head.next.key]
                self._remove(self.head.next)
                
                #add the new node
                nodeToAdd = Node(key, value, 1)
                self._add(nodeToAdd)
                self.dic[key] = nodeToAdd
                
            else:
                self.removeLeastFrequent(key, value, minFreq)
                 
    def removeLeastFrequent(self, key: int, value: int, minFreq):
        for key in self.dic:
            node = self.dic[key]
            if node.freq < minFreq:
                nodeToEvict = node
                minFreq = min(minFreq, node.freq)
            #evict the node
            self._remove(nodeToEvict)
            del self.dic[nodeToEvict.key]
            
            #add the new node
            nodeToAdd = Node(key, value, 1)
            self._add(nodeToAdd)
            self.dic[key] = nodeToAdd
    
     #remove the links
    def _remove(self, node:Node):

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    #add just before the tail node
    def _add(self, node:Node):
        tailPrev = self.tail.prev
        
        tailPrev.next = node
        node.prev = tailPrev
        self.tail.prev = node
        node.next = self.tail
            
            
            
            