#AlgoExpert problem DP
# Solutions


class Solution(object):

    #The costly dp solution! O(n^2) time | O(n) space
    def maxJumpDp(self, array):
        #init jumps array with inf and then assign the first element to 0
        jumps = [float("inf") for x in array]
        jumps[0] = 0

        #double for loop that determines if array[i] + j >= i
        # if true then set jumps[i] to the min(jumps[j] + 1, jumps[i])
        for i in range(1, len(array)):
            for j in range(0, i):
                if array[i] + j >= i:
                    jumps[i] = min(jumps[j] + 1, jumps[i])
        return jumps[-1]


    # without DP, O(n) time | O(1) space
    def maxJump(self, jumpArray):
       
        
        #init the vars with first element of the array
        maxReach = jumpArray[0]
        steps = jumpArray[0]
        jumps = 0

        for x in range(1, len(jumpArray)):

            # when we reach the end, return jump + 1
            if x == len(jumpArray) - 1:
                return jumps + 1

            #get the maxReach which is the max of maxReach and the current element of maxReach + counter x
            maxReach = max(maxReach, jumpArray[x] + x)
            
            #decrease by 1
            steps -= 1
            
            #whenever steps is 0, we must jump and reinit the steps var
            if steps == 0:
                jumps += 1
                steps = maxReach - x
