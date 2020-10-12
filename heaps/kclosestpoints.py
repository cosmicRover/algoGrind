import heapq

'''
The distance betwwen two points in a graph can be found using pythagorean thrm
Time O(nlogn) | Space O(n)
'''

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        #use pyhthagorean thrm to figue out eculedian distance
        #we will store tuple with distance as the heap valuse
        h = []
        
        for point in points:#takes n time
            x, y = point
            srt = (x**2 + y**2)**(1/2) #used pythagorean thrm to find distance
            heapq.heappush(h, (srt, x, y)) #takes log n time
            
        ans = []
        for i in range(K): #takes k'th time
            if h:
                _, x, y = heapq.heappop(h) # log n time
                ans.append([x, y])
            
        return ans
        
        