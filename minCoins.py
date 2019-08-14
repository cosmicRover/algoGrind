# Time O(nc) where c is the number of coins we need to go through
# Space O(n)


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        #init the inf array of len amount
        coinsArray = [float("inf") for num in range(amount + 1)]

        #always set the first element to 0
        coinsArray[0] = 0

        """the formula is to try and find the minimum number of coins to get to a given sum
        on each iteration we check if the given coin is <= to the amount (starting point fo the formula),
        if true then we access that specific element from the coinsArray and assign it the minimum
        of previously assigned value or 1+ amount - coin (1+coinsArray[4-2])
        """

        for coin in coins:

            for amount in range(len(coinsArray)):

                if coin <= amount:
                    coinsArray[amount] = min(
                        coinsArray[amount], 1+coinsArray[amount - coin])

        return coinsArray[amount] if coinsArray[amount] != float("inf") else -1
