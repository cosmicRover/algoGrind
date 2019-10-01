# leetcode 146 LRU cache
# could use Double LL to solve it. Alas, I couldn't get DLL version working as expected.
# ANd I later founnd out that it was due to a lack of information from the question....


# a regular DLL node with prev, next and holds key, value
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()  # kv pairs

        # init head and tail to 0:0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # link the head and tail together
        self.head.next = self.tail
        self.tail.prev = self.head

    # if key exixts, "remove" it from dict and return the value, else -1
    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        # if key already exists, remove the key
        if key in self.dic:
            self._remove(self.dic[key])

        # add the node to LL and dict
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n

        # if count exceeds capacity, remove the node after head
        # and delete the dict element as well
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    # disconnects a node's prev and next links
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # add just before tail node
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
