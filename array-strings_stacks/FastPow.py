'''
Fast power, Recursive solution
Time O(log N) | Space O(1)
'''

class Solution(object):
    def myPow(self, a, b):
        if b < 0 :
            return 1 / self.helper(a, -b)
        else:
            return self.helper(a, b)
    
    def helper(self, a, b):
        if b == 0: return 1
        
        half = self.helper(a, b // 2) #break down to halves
        
        if b % 2 == 0:
            return half * half #if no left over, we can return half * half since they will be indentical
        
        else:
            return half * half * a #if leftover, multiply with original number
    
    
# Exponential run time 
#     def myPow(self, x: float, n: int) -> float:
        
#         if x == 0: return 0
#         if n == 0: return 1
        
#         if n > 0:
#             num = 1
#             for _ in range(n):
#                 num = num * x
#             return num
        
#         if n < 0:
#             num = 1
#             for _ in range(n*-1):
#                 num = num * x
                
#             return 1/num
        