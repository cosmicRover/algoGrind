class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        '''
        find max area of a cut approach. sort with h, w, 0, cuts => find the max difference between two cuts. area is the multiplication of the two
        
        time O(n log n) | space O(n)
        
        '''
        #sort 0, h, w cuts. inserting 0 to make sure subtracting works later on
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        horizontalCuts.sort()
        verticalCuts.sort()

        #find the max difference between two consecutive cuts
        maxh = float("-inf")
        maxv = float("-inf")

        for i in range(1, len(horizontalCuts)):
            maxh = max(maxh, horizontalCuts[i] - horizontalCuts[i-1])

        for i in range(1, len(verticalCuts)):
            maxv = max(maxv, verticalCuts[i] - verticalCuts[i-1])

        # the mod is for very high numbers only
        return (maxh * maxv) % (10**9 + 7)
