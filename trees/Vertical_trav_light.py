# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> [[int]]:

        if not root:
            return

        #lighter version of vertical node, row, col vertical trav + post-order
        #col is only needed if you need to sort the items after-wards

        dic = {}  # since we are not saving col, a regular dic is fine
        queue = [(root, 0)]

        while queue:
            for _ in range(len(queue)):

                node, row = queue.pop(0)

                if row not in dic:
                    dic[row] = []

                dic[row].append(node.val)

                #left: row-1, right: row+1
                if node.left:
                    queue.append([node.left, row-1])

                if node.right:
                    queue.append([node.right, row+1])

        res = []
        for x in sorted(dic.keys()):  # get the keys in sorted order, and return it
            res.append(dic[x])

        return res
