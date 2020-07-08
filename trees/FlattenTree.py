'''
Time O(N) | In place return
***Always keep a pointer to the previous element whenever you need to modify links
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        nodes = self.bfs(root)
       
    
    def bfs(self, node):
        q = [node]
        
        #keep a prev pointer t stitch the nodes
        prev = None
        
        while q:
            item = q.pop()
            
            if item.right:
                q.append(item.right)
            
            if item.left:
                q.append(item.left)
                
            #check if prev exists first
            if prev:
                prev.right = item
                item.left = None
                prev.left = None
                
            prev = item  
        return