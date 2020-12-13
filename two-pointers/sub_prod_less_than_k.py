class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        two pointer left -> right
        as we go to the right, we build and store the product of the elements
        as long as the product is less than target, we can denote that part
        of the array to be accepted. 
        If we encounter a product more than target, we can divide to get the 
        original value
        
        Time O(n) | Space O(1)
        '''
        
        ans = 0
        prod = 1
        left = 0 
        
        for right in range(len(nums)):
            #save the product
            prod *= nums[right]
            
            #check if prod is within target aka "<", if not increment left
            while prod >= k and left <= right: #catch up to the right side
                prod /= nums[left] #dividing by the left as to remove the multiplicative effect
                left += 1
            ans += right - left + 1 #counts the elements in the subarray
            # print(nums[left:right+1]) gets the actual subarray
        return ans
        
    '''
    this is a brute force execution
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = []
        
        for i in range(len(nums)):
            if nums[i] < k:
                ans.append([nums[i]])
                
                #try to expand
                right = i+1
                while right < len(nums):
                    arr = nums[i:right+1]
                    prod = self.getProduct(arr)
                    
                    if prod < k:
                        ans.append(arr)
                        right += 1
                    else:
                        break
                        
        return len(ans)
    
    def getProduct(self, arr):
        ans = 1
        for i in arr:
            ans *= i
            
        return ans
    '''