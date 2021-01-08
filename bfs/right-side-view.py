# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        level order bfs pop(0)
        
        the last item on a left to right traversal is the rightmost node
        or a single left node. we just appended that to the ans array
        
        '''
        
        if not root: return
        
        q = [root]
        ans = []
        
        while q:
            level = len(q)
            last = None
            
            for _ in range(level):
                node = q.pop(0)
                last = node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            ans.append(last)
            
        return ans
                
                
        