class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        UMPIRE
        
        Understand:
        test cases:
        [1,2,3,1,1,6], k = 3 => 1 + 6 + 5 = 12
        
        given an array and k, pick at most k values from right or left
        
        Match:
        DP pattern with memoizing largest value possible
        
        Plan:
        Since we can only take k elements from left or right, we start off
        with the sum on the left and remember it. Later we sub from the left
        and add from the right while remembering max possible value
        
        implement:
        '''
        leftScore = sum(cardPoints[:k])  # sum k'th values from the left
        rightScore = 0
        size = len(cardPoints)

        #start off from the left
        maxScore = leftScore

        i = k-1
        while i >= 0:
            #subtract from the keft while add from the right
            rightScore += cardPoints[size - (k-i)]
            leftScore -= cardPoints[i]

            val = (rightScore+leftScore)

            maxScore = max(maxScore, val)
            i -= 1

        return maxScore

        '''
        Review:
        brute foce times out, use two pointers approach to sub/add values
        
        Evaluate:
        time O(n) | space O(1)
        '''
