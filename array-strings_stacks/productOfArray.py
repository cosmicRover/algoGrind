# leetcode 238
# Time O(n) | Space O(1)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # init array with value 1 which is len(nums) long
        returnArray = [1] * len(nums)

        # keeps track of current product
        product = 1

        # pass through the array one time and store product to returnArray while multiplying product with nums[x]
        for x in range(len(nums)):

            returnArray[x] = product
            product *= nums[x]

        # reinit product to 1
        product = 1

        # go through the array backwards and this time multiply returnArray elements with product
        # while multiplying product with num[y]
        for y in range(len(nums) - 1, -1, -1):
            returnArray[y] *= product
            product *= nums[y]

        return returnArray
