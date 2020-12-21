class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        fast/slow pointer approach. slow.next ->fast.next.next 
        similar approach as finding a cycle in an LL
        
        time O(logN) with proof | Space O(1)
        '''
        slow = n
        fast = n
        
        while True:
            slow = self.squareNum(str(slow)) #move at 1 speed
            
            #moves at 2 speed by recursively calling find square on previous value
            fast = self.squareNum(str(self.squareNum(str(fast)))) 
            
            #this is our goal
            if slow == 1 or fast == 1: 
                return True
            
            #if we have a cycle, then we can't reach our goal
            if slow == fast:
                return False

    def squareNum(self, x):
        s = 0
        for i in str(x):
            n = int(i)**2
            s += int(n)
        return s

# class Solution:
# this is a solution with extra space
#     def isHappy(self, n: int) -> bool:
#         if n == 1: return True
        
#         dic = set()
#         while True:
#             val = self.squareNum(n)
#             if val == 1:
#                 return True
#             if str(val) in dic:
#                 return False
#             dic.add(str(val))
#             n = val
            
    
#     def squareNum(self, x):
#         s = 0
#         for i in str(x):
#             n = int(i)**2
#             s += int(n)  
#         return s
        