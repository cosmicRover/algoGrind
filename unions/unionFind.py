#leetcode 684


class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:

        maxValue = float("-inf")

        #find the max node value
        for start, end in edges:
            maxValue = max(maxValue, start, end)

        #create a table to store root values with the length of maxValue + 1
        root = [i for i in range(maxValue + 1)]

        #iterate through the edges, see if there's a match, if not union it
        for start, end in edges:
            if self.find(root, start) == self.find(root, end):
                return[start, end]
            self.union(root, start, end)

    def union(self, root, start, end):
        root[self.find(root, end)] = self.find(root, start)
        print(root)
        return

    #loop through the root table and return the connection
    def find(self, root, start):
        node = start
        path = []

        while node != root[node]:
            path.append(node)
            node = root[node]

        #connection?
        ans = node

        while path:
            node = path.pop()
            root[node] = ans

        print("root ans -> ", ans)
        return ans
