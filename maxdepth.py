# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        height = 0

        if root is None:
            return height

        while True:
            # nodeCount keeps track of the queue length
            nodeCount = len(queue)

            # when it reaches 0, it means that there are no more children
            if nodeCount is 0:
                return height

            # for each iteration, increase the height by 1
            height += 1

            # while nodeCount is > than a 0,
            # we pop the first element from the queue
            # then we append the left/right node
            # and we decrease the nodeCount by 1
            while nodeCount > 0:
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                nodeCount -= 1

    # the recursive solution, just calls itself using the left/right node
    # it is important to +1 to the recursive call as it tracks the depth****
    def maxDepthRecursive(self, root):
        # edge case
        if not root:
            return 0

        # if left and right child dont exist, return the max between left and right
        if not root.left or not root.right:
            return max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right)) + 1

        # just change the max to min() and it will return the minimum depth of the given tree
        else:
            return max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right)) + 1
