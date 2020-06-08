class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        res = []
        n = len(nums)

        self.backtrack(nums, 0, n-1, res)

        return res

    def backtrack(self, arr, left, right, res):

        if left == right:
            res.append(arr[:])  # doesn't work without [:]
        else:

            for i in range(left, right+1):
                # swap left with index
                arr[left], arr[i] = arr[i], arr[left]

                # recursively call backtrack
                self.backtrack(arr, left+1, right, res)

                # swap back for backtrack
                arr[left], arr[i] = arr[i], arr[left]
