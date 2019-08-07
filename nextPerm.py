class Solution:
    # Time On
    # Space O1

    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
			# Reverse iterate until a digit is greater than the previous one
            if nums[i] > nums[i-1]:
				# Find the smallest digit bigger than the previous digit
                next = i
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i-1] and nums[j] < nums[next]:
                        next = j

			#Swap previous and next ascending, and sort the rest
                nums[i-1], nums[next] = nums[next], nums[i-1]
                nums[i:] = sorted(nums[i:])
                return
        else:
			# Number is reverse sorted and maximum possible
            nums.reverse()
