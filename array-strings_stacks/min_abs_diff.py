'''
These types of problems need to be looked through the constraints first before approaching
connstarints: 
1) a, b from arr
2) a < b (hinting at sorting)
3) b - a indicates the minimum diff we can expect from any two items on arr

Time O(nlogn) for sorting | Space O(#min sub lists possible)
'''

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        minV = float("inf")
        ans = []
        
        #since we have things sorted, we can start from index 1
        for i in range(1, len(arr)):
            #get the diff we are looking for
            diff = arr[i]-arr[i-1]
            
            #make the current apir
            current_pair = [arr[i-1], arr[i]]
            
            #compare with current min and see if we have a new min
            #if so, we just reset ans
            if diff < minV:
                minV = diff
                ans = [current_pair]   
            #otherwise, append the current pair
            elif diff == minV:
                ans.append(current_pair)
                
        return ans