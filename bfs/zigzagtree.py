# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        bfs level order traversal approach. pop(0)
        '''
        if not root: return
        
        ans = []
        ladder = 1
        q = [root]
        
        while q:
            level = len(q)
            temp = []
            
            for _ in range(level):
                
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
            
            #append regularly or in reverse based on ladder being odd or even
            if ladder % 2 > 0:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            
            ladder += 1
            
        return ans