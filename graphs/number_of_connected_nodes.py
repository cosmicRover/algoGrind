class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        graph traversal problem. only traverse for nodes haven't seen yet
        
        time O(n) | space O(maximum width of graph)
        '''

        adj = {}

        for i in range(n):
            adj[i] = []

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        count = 0

        for i in range(n):
            if i in visited:
                continue

            q = [i]

            while q:
                node = q.pop()
                visited .add(node)

                for v in adj[node]:
                    if v not in visited:
                        q.append(v)

            count += 1

        return count