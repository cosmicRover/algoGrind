# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        '''
        P   NLR
        I   LNR
        PO  LRN
        
        - root node is the last element on postorder
        - the index of root node inside the inorder array divides left and right subtree
        - repeat until left > right
        
        time O(n) | space O(n)
        '''
        dic = {}
        for i, v in enumerate(inorder):
            dic[v] = i
            
        return self.build(dic, postorder, 0, len(inorder)-1 )
            
    def build(self, dic, post, left, right):
        
        if left > right:
            return
        
        #get the enxt root from postorder
        val = post.pop()
        root = TreeNode(val)
        
        #get left/right division index from inorder
        mid = dic[val]
        
        #recurse on the right and left subtree
        root.right = self.build(dic, post, mid+1, right)
        root.left = self.build(dic, post, left, mid-1)
        
        return root