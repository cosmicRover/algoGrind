class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        modified binary search approach. kth element -> adjust left < k
        
        since the array is pre-sorted, we can use binary search to find the k'th missing.
        
        time O(log n) | space O(1)
        '''
        
        left = 0; right = len(arr) -1;
        
        while left <= right:
            mid = (left+right)//2
            
            #the arr[mid] - mid - 1 is used to substitute for missing numbers
            if arr[mid] - mid - 1 < k: 
                left = mid + 1
            else:
                right= mid - 1
                
        return left + k
        
    
    
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         '''
#         range is 1 to n
        
#         time O(n) | sapce O(n for the temp arr)
#         '''
#         #get biggest and init a temp to hold visited vals
#         temp = [-1] * arr[-1]
        
#         #visit the vals
#         for x in arr:
#             temp[x-1] = x
            
#         print(temp)
            
#         #extrack kth item
#         tempk = k
#         for i, v in enumerate(temp):
#             if v == -1:
#                 tempk -= 1
                
#             if tempk == 0:
#                 return i+1
            
#         else:
#             return len(temp) + tempk