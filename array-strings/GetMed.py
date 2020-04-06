class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        arr = nums1 + nums2
        
        #do a merge sort
        self.mergeSort(arr)
        
        return self.result(arr)
        
        
    
    def result(self, nums1):
        isEven = self.isEven(nums1)
        
        if isEven:
            index = self.getEvenMid(nums1)
            sums = 0
            while index:
                item = index.pop()
                sums += nums1[item]
            return sums/2.0
        
        else:
            index = self.getOddMid(nums1)
            return nums1[index]
            
        
    def mergeSort(self, arr):
        if len(arr) > 1:
            #setups
            m = len(arr) // 2
            left = arr[:m]; right = arr[m:]
            
            #recursive calls to divide
            self.mergeSort(left)
            self.mergeSort(right)
            
            #start merging
            arr.clear()
            
            while left and right:
                if left[0] < right[0]:
                    arr.append(left[0])
                    left.pop(0)
                elif left[0] >= right[0]:
                    arr.append(right[0])
                    right.pop(0)
                    
            for i in left:
                arr.append(i)
            
            for i in right:
                arr.append(i)
            
            
    def isEven(self, l):
        return True if len(l) % 2 == 0 else False
    
    def getEvenMid(self, l):
        mid = len(l) // 2
        return [mid-1, (mid+1)-1]
    
    def getOddMid(self, l):
        return len(l) // 2
        
        
        