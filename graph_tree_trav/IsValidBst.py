# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Time O(n + n) -> O(n) | Space O(number of nodes) -> O(n)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        '''
        step 1, get inorder traversal. In inOrderTrav, a BST is represented in complete
        with an ascending order
        node.left -> node -> node.right
        '''
        res = self._inOrderHelper(root, [])
        
        '''
        step 2, check if the values are in ascending order. 
        If not, return false. In this case even if it's equal, return false
        '''
        for i in range(len(res) - 1):
            if res[i] >= res[i+1]:
                return False
            
        return True
        
    
    #in order recursive
    def _inOrderHelper(self, node, res):
        if not node:
            return 
    
        self._inOrderHelper(node.left, res)
        res.append(node.val)
        self._inOrderHelper(node.right, res)
        
        return res
