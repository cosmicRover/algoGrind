'''
When merging two intervals i.e. [1, 3] and [2, 5] : you can check if you should merge
by comparing end time and start time and see if end time >= start time (3 >= 2)
then you may reshape the lowwer and upper values by taking min/max of start and end
times from the two intervals

Time O(n log n) | Space O(n)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals
        
        ans = []
        
        #sort the intervals by starting time
        intervals.sort(key=lambda x:x[0])
        
        for i in range(len(intervals)):
            #if ans is empty, just append the first item
            if not ans:
                ans.append(intervals[i])
                continue
                
            #compare with the last appended value's end time and current start time
            if ans[-1][1] >= intervals[i][0]:
                
                #reshape the last appended item's boundary.
                #start will be min while end will be max
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
                ans[-1][0] = min(ans[-1][0], intervals[i][0])
            else:
                #if they dont cross interval, just append them as regular
                ans.append(intervals[i])
                
        return ans
        