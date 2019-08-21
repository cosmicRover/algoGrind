# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        queue = collections.deque([root])
        firstPass = False
        
        while queue[0]:
            node = queue.popleft()
            
            if node.right.val is x or node.right.val is y:
                node = queue.popleft()
                if node.right.val is x or node.right.val is y:
                    return True
                
            if node.left.val is x or node.left.val is y:
                node = queue.popleft()
                if node.left.val is x or node.left.val is y:
                    return True
            
            queue.append(node.left)
            queue.append(node.right)