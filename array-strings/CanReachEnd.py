class Solution:
    
    #time O(n) and O(1) space
    def canJump(self, nums: [int]) -> bool:
        
        mJump = 0 #remembers max jump value
        
        for index, value in enumerate(nums):
            print(index, value)
            
            #if index is ever bigger than max jump range, we cant reach the end
            if index > mJump: return False
            
            #mJump is always the max of mJump and index+value (index + value since together they determine how far we can jump)
            mJump = max(index+value, mJump)
            print(mJump)
        
        return True