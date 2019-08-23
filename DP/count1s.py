class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # DP solution
        # Time and space O(n)
        # base case 0
        array = [0]

        # if > 0, insert a 1
        if num > 0:
            array.append(1)

        """
        pass through once starting frome range 2
        formula is -> value in array[x/2] + x%2 where x is the current counter value
        will always equal to the number of 1s resides within the current binary vlaue
        for example: array[2/2] + 2%2
                     array[1] -> 1 + 0 = 1
                     
                     array[7/2] + 5%2
                     array[3] -> 2 + 1 = 1
        """

        for x in range(2, num + 1):

            array.append(array[x/2] + x % 2)

        return array

        # brute force: get binary value, slice ot and count the number of 1's
        # for x in range(1, num + 1):
        #     binaryValue = bin(x)
        #     binaryValue = binaryValue[2:]
        #     oneCounter = binaryValue.count('1')
        #     array.append(oneCounter)
        # return array
