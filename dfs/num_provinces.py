class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        dfs approach. count the connected cities as one + disconnected
        
        time O(n^2) | O(n+m) n is for the adjdic and m for stack
        '''
        #made this into an adjacency list since I find it easier to work with
        adjdic = {}
        for i, v in enumerate(isConnected):
            connections = []
            for j, v in enumerate(v):
                if i == j:
                    continue

                if v == 1:
                    connections.append(j)

            adjdic[i] = connections

        #perfom dfs on the adjlist
        count = 0
        visited = set()

        for i in range(len(isConnected)):
            if i in visited:
                continue

            stack = [i]

            while stack:
                node = stack.pop()
                visited.add(node)

                for neighbor in adjdic[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            count += 1

        return count