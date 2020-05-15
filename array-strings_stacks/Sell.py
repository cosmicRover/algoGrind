class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)

        if length == 0:
            return 0

        #init temp as the last value of the list
        temp = prices[length-1]

        res = 0

        # traversing backwards
        for i in range(length-1, -1, -1):

            # temp holds the max
            temp = max(temp, prices[i])

            # if max - current price > res,
            #then assign res to that value
            if temp - prices[i] > res:
                res = temp - prices[i]

        return res
