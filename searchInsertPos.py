# Binary search solution


class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:

        l, r = 0, len(nums) - 1

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        # divide the array from the mid and carry out the search
        while l < r - 1:

            mid = (l + r)//2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                l = mid

            else:
                r = mid

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        return r
