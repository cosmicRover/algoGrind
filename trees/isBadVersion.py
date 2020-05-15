# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# can use isBadVersion(version) to check for a bad version

'''
This is a simple problem but confusingly worded.
This basically boils down to given a numbr,
I want you to find a number using the isBadVersion(number)
method. This is done in O(log(n)) in binary tree
'''

'''
Time O(log(n)) | Space O(1)
'''


class Solution:
    def firstBadVersion(self, n):

        # binary search procedure
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right-left) // 2

            if isBadVersion(mid) == False:
                left = mid + 1

            else:
                right = mid - 1

        return left # we return left since we want the parent of the branch
