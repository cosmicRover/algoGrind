#branch bfs trav requires a loop of len(queue) to completely 
#empty out a queue before appending new items
#Time O(v+e till the desired level) | Space (seen + movies) consisting of ids

class Solution:
    def watchedVideosByFriends(self, watchedVideos: [[str]], friends: [[int]], id: int, level: int) -> List[str]:
        queue = [id]
        count = 0
        seen = set(queue)
        
        while queue and count != level: #bfs, level by level till the desired level
            for _ in range(len(queue)):
                node = queue.pop(0)
                
                for x in friends[node]:
                    if x not in seen:
                        seen.add(x)
                        queue.append(x)
                
            count += 1
                        
        print(queue)
                
        movies = dict()
        for i in queue: 
            for m in watchedVideos[i]: 
                movies[m] = movies.get(m, 0) + 1 #inc by 1
            
        print(movies)
        
        return [k for v, k in sorted((v, k) for k, v in movies.items())] #for each k, v pair, sort by value of a given key