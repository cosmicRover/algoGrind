# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time O(N + Queue) linear for nodes and a search of none values | Space O(nodes) where queue stores the nodes 

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # edge case if root is none
        if not root: return False

        # use a queue to go level by level like bfs
        queue = collections.deque([root])
        
        # while queue is not None 
        while queue[0]:
            node = queue.popleft() # pop the left most

            # and append their left + right nodes
            queue.append(node.left)
            queue.append(node.right)
            
        # if any nodes left in the queue, it will be None
        # if any found, return false
        for noneNode in queue: 
            if noneNode: return False
        return True
