class Solution(object):

    def findPeakElement(self, nums):

        #insert elemnents to make it at least be divisible by 2
        nums = [-2**32]+nums+[-2**32]

        l, r = 0, len(nums)-1

        while l <= r:

            #since we do binary search, find middle
            m = (l+r) // 2

            #check for target
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m - 1
            else:
                #only look at right side apparently and re-adjust l, r
                if nums[m] < nums[m+1]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
