#This is for binary trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # pre-> append -> dive -> dive
        # post -> dive -> dive -> append
        # inord -> dive -> append -> dive
        
        # init return array and the stack
        array = []
        stack = [root]

        # while stack has a len of > 0
        while len(stack):
            node = stack.pop()
            
            # if node is not None
            # for some reason, appending right first gets the right answere here
            if node:
                array.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
        return array
    
    
 #This is for graphs

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# A preorder traversal is when you visit the left most braches throughly before moving to the right branches.
# But first, you must visit the root
class Solution:
    
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        rArr = []
    
        while stack:
            
            node = stack.pop()
            
            if node != None:
                rArr.append(node.val)
                for x in reversed(node.children): # reversed, otherwise it vists the right side first
                    stack.append(x)
                
        return rArr