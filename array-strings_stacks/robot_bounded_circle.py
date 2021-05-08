class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        change directions one way relative to the current position with mod
        for this problem, the goal is to see if direction changes. as long
        as the direction changes, it is bound to come back to the starting node
        
        time O(n) | space O(1)
        
        '''
        #4 directions N         E       S       W
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = 0
        y = 0
        index = 0

        for i in instructions:
            #turn left from current position using index
            #index = (index + index of the direction element) % total number of directions
            #this will turn direction clock-wise
            if i == "L":
                index = (index+3) % 4

            elif i == "R":
                index = (index+1) % 4

            else:
                #increment current step
                x += directions[index][0]
                y += directions[index][1]

        return (x == 0 and y == 0) or index != 0
