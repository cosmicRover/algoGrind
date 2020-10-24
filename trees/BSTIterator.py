# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Remember PIPO and in-order traversal for BST
Time O(N) | Space O(N)
'''


class BSTIterator:

    def __init__(self, root: TreeNode):
        #in-order search to get all the nodes
        self.stack = self.inOrder(root, [])
        self.stack = self.stack[::-1] 
        #reversed it for smaller values on the right side, can reverse PIPO to achieve the exact effect
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack.pop()
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
    
    def inOrder(self, root, arr):
        '''
        P   NLR
        I   LNR
        PO  LRN
        '''
        if root:
            if root.left:
                self.inOrder(root.left, arr)
            arr.append(root.val)
            if root.right:
                self.inOrder(root.right, arr) 
        return arr

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()