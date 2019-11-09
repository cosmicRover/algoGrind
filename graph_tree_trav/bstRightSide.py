# leetcode problem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        currentNodeBranches = [root]
        returnArray = []

        while currentNodeBranches:

            nextBranchesToExplore = []

            for node in currentNodeBranches:
                if node.left:
                    nextBranchesToExplore.append(node.left)
                if node.right:
                    nextBranchesToExplore.append(node.right)

            # append the last item from currentBranch
            returnArray.append(currentNodeBranches[-1].val)

            # currentBranch becomes the next branch
            currentNodeBranches = nextBranchesToExplore

        return returnArray
