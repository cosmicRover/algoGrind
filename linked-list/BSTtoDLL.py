'''
The trick here was to use the left/right pointers to substitue for next and prev.
The ordered nodes from BST can be retrieved by using Inorder traversal

Time O(n) | Space O(n)
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        P   NLR
        I   LNR <- will give you sorted items on a BST
       PO   LRN
        '''
        
        if not root: return
        
        #in order traversal
        nodes = self.inOrder(root, []) 
        
        #compose the doubly linked list
        dummy = Node(nodes[0])
        head = dummy
        
        #if only one node, just connect head with dummy
        if len(nodes) == 1:
            head.right = dummy
            dummy.left = head
            return dummy
        
        for i in range(1, len(nodes)):
            #save prev
            prev = head
            
            #set right
            head.right = Node(nodes[i])
            
            #set right's left
            head.right.left = prev
            
            #increment head
            head = head.right
        
        #connect head with dummy and dummy with ehad
        head.right = dummy
        dummy.left = head
        
        return dummy
    
    def inOrder(self, root, nodes):
        if root:
            if root.left:
                self.inOrder(root.left, nodes)
            nodes.append(root.val)
            if root.right:
                self.inOrder(root.right, nodes)
        return nodes