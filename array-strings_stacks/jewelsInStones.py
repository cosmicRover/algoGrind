class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for x in S:
            if x in J:
                count += 1

        return count
