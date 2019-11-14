"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

# time and space complexity is terrible
# just used this as a practice to convert BST to a DLL
# Gotta find more optimized solution
# a more optimized approach would be to resturucture them into DLL
# while traversing
        
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def setTail(self, val):
        self.tail = Node(val)
        
    def setHead(self, val):
        self.head = Node(val)
        self.tail = self.head
            
    def insertNode(self, val):
        if not self.head:
            self.setHead(val)
            return
        
        current = self.head
        while current.right:
            current = current.right
            
        new = Node(val)
        current.right = new
        new.left = current
        
        self.tail = new
        
    def attachTailToHead(self):
        head = self.head
        tail = self.tail
        
        head.left = tail
        tail.right = head
        
    
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        if not root:
            return
        
        res = self.inOrderTrav(root, [])
        
        l = DLL()
        
        for i in range(len(res)):
            l.insertNode(res[i])
            
            if i == len(res) - 1:
                print(i)
                l.attachTailToHead()
                
        return l.head
        
    
    #inorder gets ascending BST values
    def inOrderTrav(self, node, res):
        if not node:
            return 
        
        self.inOrderTrav(node.left, res)
        res.append(node)
        self.inOrderTrav(node.right, res)
        
        return res