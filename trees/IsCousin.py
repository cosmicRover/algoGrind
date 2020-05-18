'''
Time O(n) | Spce O(n)
'''


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        q = [root] #bfs queue
        p = {} #holds the parents and leves
        level = 1

        while q:

            temp = []

            for _ in range(len(q)):

                node = q.pop(0)
                print(node.val)

                if node.left:
                    p[node.left.val] = (level, node.val)
                    temp.append(node.left)

                if node.right:
                    p[node.right.val] = (level, node.val)
                    temp.append(node.right)

            q = temp
            level += 1

        return self.matchParent(p, x, y)

    def matchParent(self, p, x, y):
        if x not in p or y not in p: #prevents key error
            return False

        return p[x][0] == p[y][0] and p[x][1] != p[y][1]
