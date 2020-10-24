'''
The trick here is to figure out the steps to connect the left/right nodes
in place with pointers.

Time O(n) since we only go through each node once| Space O(1)

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        #set up a node
        node = root
        
        #for each node, we need to attach it to the right side of root
        while node:
            
            #if node has a left side
            if node.left:
                
                #get the rightmost leaf of node.left
                rightm = node.left
                while rightm.right: #ensuring right isnt none
                    rightm = rightm.right
                    
                #reconnect rightm with node.right
                rightm.right = node.right
                
                #since we are on left now, transfer to right
                node.right = node.left
                
                #set left to None
                node.left = None
                
            #reset node to right
            node = node.right