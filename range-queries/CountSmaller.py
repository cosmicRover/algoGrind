class Solution:

    def getLSB(self, num):
        return num & (-num)

    def update(self, BIT, index, length):
        while index <= length:
            BIT[index] += 1
            index += self.getLSB(index)

    def getSum(self, BIT, index):
        sum = 0
        while index:
            sum += BIT[index]
            index -= self.getLSB(index) # keep incrementing downward
        return sum

    def countSmaller(self, nums: [int]) -> [int]:
        #init a rank dictionary. It will give an ascending key to the sorted
        #elements (from low to high) so we can access the smallest elements later
        rank = {val: i+1 for i, val in enumerate(sorted(nums))}
        length = len(nums)
        response = []

        BIT = [0] * (length + 1) #init an indexed tree with an extra 0

        #a reversed loop of the nums
        for x in reversed(nums):
            response.append(self.getSum(BIT, rank[x] - 1)) #TODO: needs clarification
            self.update(BIT, rank[x], length)

        return response[::-1]
