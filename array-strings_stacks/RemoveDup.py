'''
Time O(N) | Space O(1)
'''


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:

        prev = None
        count = 0

        while count != len(nums):
            if prev == None:
                prev = nums[count]

            else:
                if prev == nums[count]:
                    del nums[count]
                    count -= 1  # the key is to decrement once deleted

            prev = nums[count]
            count += 1
