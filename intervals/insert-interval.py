class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Since the intervals are overlap free and pre-sorted, we really need to think of a linear algorithm
        
        time O(n) no sorting at all | space O(n) for ans array
        '''
        
        ans = []
        i = 0
        
        #skip to the position that newInterval can be inserted
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
            
        #reshape newInterval so that it is merged with the other intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        #append the interval after reshaping
        ans.append(newInterval)
        
        #add the remaining
        while i < len(intervals):
            ans.append(intervals[i])
            i+= 1
            
        return ans
            

#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         '''
#         exactly the same as merge interval
#         time O(n log n) | space O(n)
        
#         '''
#         #this is identical to merge intervals, we append the new interval
#         intervals.append(newInterval)
#         intervals.sort(key=lambda x:x[0])
        
#         ans = [intervals[0]]
        
#         for i in range(1, len(intervals)):
#             last = ans[-1]
#             lEnd = last[1]
            
#             cStart = intervals[i][0]
#             cEnd = intervals[i][1]
            
#             if lEnd >= cStart:
#                 if cEnd > lEnd:
#                     ans[-1][1] = cEnd
#             else:
#                 ans.append(intervals[i])
 
#         return ans