"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# A post traversal is when you visit the left most braches throughly before moving to the right branches and eventually visiting root
# recursive solution from left to right, no need for reversing
class Solution:
    
    def postorder(self, root: 'Node') -> [int]:
        rArr = []
        return self._postOrder(rArr, root)
    
    def _postOrder(self, rArr, node):
        if node:
            if node.children:
                for x in node.children:
                    self._postOrder(rArr, x)
            print(node.val)
            rArr.append(node.val)
            return rArr
            