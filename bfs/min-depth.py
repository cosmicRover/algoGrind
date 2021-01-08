# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        level order bfs approach. pop(0)
        
        time O(n) | space O(1)
        '''

        if not root: return 0
        
        depth = 0
        
        q = [root]
        
        while q:
            level = len(q)
            depth += 1
            
            for _ in range(level):
                node = q.pop(0)
                
                #first sign of a leaf node, we return depth
                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        