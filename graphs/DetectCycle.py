class DetecyCycle:
    def detect_cycle(self, nums:[[int]]):

        #init ds to hold graph and visited values
        #can reduce the amount of unnecessary space by having # of nodes inputted directly
        #or validating some other way (with sets perhaps)
        graph = [set() for _ in range(len(nums))]
        visited = [0] * len(nums)


        #populate graph
        for s, d in nums:
            graph[s].add(d)

        #bfs to search through the entire graph 
        #since no start node is provided, assuming we will start at node 0
        queue = [0]
        while queue:

            item = queue.pop(0)
            visited[item] = 1

            for neighbor in graph[item]:
                if visited[neighbor] == 1:
                    print("has cycle at node:", neighbor, "redundent connection at node:", item)
                    return True
                queue.append(neighbor)

        print("no cycle")
        return False


dc = DetecyCycle()
input_arr = [[0,1], [1,3], [1,2], [1,4], [3,7], [2,6], [7,8], [4,5],
            [6,5], [8,9], [5,9], [9,8]]
print(dc.detect_cycle(input_arr))