class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        stack circular approach with index.
        pre-processing with dic won't work since nums are not unique and it's circular.
        
        two loop strategy:
        - the first loop will get the next greater element
        - with the help of left-over items on stack, the second loop will 
            produce next greater in a circular manner
        
        time O(at most 2n) | space O(n)
        '''
        size = len(nums)
        ans = [-1] * size
        stack = []
        
        for _ in range(2):
            for index, val in enumerate(nums):
                if not stack:
                    stack.append(index)
                    continue

                #compare and populate next gerater value using index from stack
                while stack and val > nums[stack[-1]]:
                    small_index = stack.pop()
                    ans[small_index] = val

                stack.append(index)
            
        return ans