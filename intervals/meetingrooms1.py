'''
Time O(n log n) | Space O(1)
'''

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0]) #sorting intervals by start time
        
        for i in range(1, len(intervals)):
            forward = intervals[i]
            backward=intervals[i-1]
            
            '''
            the idea is that, for each meeting to start, the previous meeting
            needs to be ended. So we compare previous end time to currennt start time
            '''
            if backward[1] > forward[0]:
                return False
            
        return True