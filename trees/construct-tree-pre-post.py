# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        '''
        P   NLR
        I   LNR
        PO  LRN
        
        divide and conquer approach.
        - root is at index 0 in preorder and last index at post order
        - the item at index 1 on pre is the left node and the left subtree
          consists of post[: location of item 1 from pre] while the right
          subtree is at post[location of item 1 from pre:]
        - keep dividing, and in the end compose tree
        
        time O(n^2) | space O(n)
        '''
        
        if not pre: return None
        
        #setup root
        root = TreeNode(pre[0])
        
        if len(pre) == 1: return root
        
        #identify the left node on post array
        leftIndex = post.index(pre[1]) + 1 #+1 so that the index is inclusive
        
        #keep dividing for left and right while omitting already taken indexes
        root.left = self.constructFromPrePost(pre[1:leftIndex+1], post[:leftIndex])
        root.right = self.constructFromPrePost(pre[leftIndex+1:], post[leftIndex:-1])
        
        return root