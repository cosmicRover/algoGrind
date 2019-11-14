# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time O(n) | Space O(num of nodes) -> O(n)
# in_order -> node.left, node, node.right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        
        res = self._inOrderHelper(root, [])
        return res
        
    
    def _inOrderHelper(self, node, res):
        if not node:
            return 
        
        self._inOrderHelper(node.left, res)
        res.append(node.val)
        self._inOrderHelper(node.right, res)
        
        return res
        