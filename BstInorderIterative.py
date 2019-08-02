# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # pre-> append -> dive -> dive
        # post -> dive -> dive -> append
        # inord -> dive -> append -> dive
        
        # init return array and the stack
        array = []
        stack = [root]

        # while stack has a len of > 0
        while len(stack):
            node = stack.pop()
            
            # if node is not None
            # for some reason, appending right first gets the right answere here
            if node:
                array.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
        return array
    
    
    
        
    # def order(self, root, array):
    #     while root:
    #         array.append(root.val)
    #         self.order(root.left, array)
    #         self.order(root.right, array)
    #     return array
        