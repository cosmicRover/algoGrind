from collections import deque

class FirstUnique:
    '''
    use a dict to remember if a value is unique and use a queue to iterate over
    the appended array from left to right
    
    time O(1) on avergae | space O(total number of elements + unique elements)
    
    '''

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.udic = {}
        
        for x in nums:
            self.q.append(x)
            self.add(x)
        

    def showFirstUnique(self) -> int:
        while self.q and self.udic and self.udic[self.q[0]] == False:
            self.q.popleft()
            
        return self.q[0] if self.q else -1
        

    def add(self, value: int) -> None:
        if value in self.udic:
            self.udic[value] = False
            self.q.append(value)
        else:
            self.udic[value] = True
            self.q.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)