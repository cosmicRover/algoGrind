'''
Time O(ElogE + E) where ElogE is the sorting time and + E to form the MST
Space O(N) for parent dict
'''


class Solution:
    def find(self, parent, city):
        if parent[city] != city:
            parent[city] = self.find(parent, parent[city])
        return parent[city]

    def union(self, parent, c1, c2):
        root1, root2 = self.find(parent, c1), self.find(parent, c2)

        if root1 == root2:
            return False
        parent[root2] = root1  # Always join roots!

        return True

    def minimumCost(self, N: int, connections: [[int]]) -> int:

        #init parent from 1 to N+1 since node starts from 1
        parent = {city: city for city in range(1, N+1)}

        # sort graph with low to high edge weights
        connections.sort(key=lambda item: item[2])

        total = 0

        for city1, city2, cost in connections:
            #unify all the roots and update the cost
            if self.union(parent, city1, city2):
                total += cost

        print("unioned nodes => ", parent)

        # find the root node of the last node
        root = self.find(parent, N)

        #if root matches with the roots of all the other nodes (recursive call), then we have a valid answer
        #all keyword matches everything inside the expressions
        return total if all(root == self.find(parent, city) for city in range(1, N+1)) else -1
