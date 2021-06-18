class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        '''
        time O(n*n) | space O(1)
        '''

        ans = 0

        nums.sort()  # O(n log n)

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                _sum = nums[i]+nums[left]+nums[right]

                if _sum < target:
                    #if the current left to right window works, the all the spots between left and right pointer
                    #will also work. Thus, we add right-left to the ans

                    ans += right - left

                    left += 1  # increment left to find next possible value windows

                else:
                    right -= 1  # decrease the value

        return ans
