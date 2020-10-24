'''
similar to meeting room 1, the formula to figure out if a meeting overlaps with another i.e. a new room sceneario
we just need to track the earliest ending meetings via a minheap

Time O(n log n) | Space O(n)
'''

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        #sort by strat times, so we may know meeting order
        intervals.sort(key=lambda x:x[0])
        
        #our heap, to track ealriest end time
        h = []
        
        #iterate through the meetings and update
        for x in intervals:
            #we automatically add first meeting if none is going on
            if not h:
                heapq.heappush(h, x[1])
                continue
                
            #compare end time with start time
            if h[0] <= x[0]:
                heapq.heappop(h) #one meeting is done
                heapq.heappush(h, x[1]) #slotting in the next meeting
            else:#otherwise we will need a new meeting room
                heapq.heappush(h, x[1])
                
                
        return len(h) #this will contain the max amount of meeting rooms we need
                