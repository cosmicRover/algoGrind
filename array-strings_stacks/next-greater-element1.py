class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        stack find greater approach. append to stack -> empty stack when num is greater
        
        time O( size nums1 + nums2) | sapce O(size of nums1 + nums2)
        '''
        
        #pre-process items with their immediate greater value
        stack = []
        dic = {}
        
        for num in nums2:
            if not stack:
                stack.append(num)
                continue
                
            while stack and num > stack[-1]:
                small = stack.pop()
                dic[small] = num

            stack.append(num)
         
        #the rest don't have a grater value
        while stack:
            item = stack.pop()
            dic[item] = -1
        
        ans = []
        for num in nums1:
            ans.append(dic[num])
            
        return ans