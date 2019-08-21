class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #simple for loop
        for i in range(1, len(nums)):

            # if the previous value if > 0, then we add it to the current element
            # "its a game of sums, not elemensts" as the author emphasized on their post.
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)
