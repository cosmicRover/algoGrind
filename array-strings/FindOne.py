class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.findNext(n)

        return n == 1

    def findNext(self, n):
        sums = 0
        if n == 0:
            return sums

        s = str(n)
        for x in s:
            sums += int(x)**2

        return sums
