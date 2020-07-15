class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> [int]:
        if not root: return
        
        q = [root]
        res = []
        
        while q:
            
            temp = []
            m = float("-inf")
            
            for node in q:
                m = max(m, node.val)
                
                if node.left:
                    temp.append(node.left)
                
                if node.right:
                    temp.append(node.right)
                    
            q = temp
            res.append(m)
            m = float("-inf")
            
        return res