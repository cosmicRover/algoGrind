class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        '''
        this is extremely implementation heavy problem, this is sort of a brute force problem
        with only the drop method being a little bit forward thinking
        
        time o((row*col)^2) | space O(n) for the stack and the targets
        '''
        while True:
            targets = self.mark(board)
            if not targets: return board #always
            self.crush(board, targets)
            board = self.drop(board)
        
    #gte the row,col coordinates we need to crush as a set
    def mark(self, board):
        width = len(board[0])
        height = len(board)
        targets = set()
        
        for row in range(height):
            for col in range(width):
                #we need at least 3 cells to match horizontally or vertically
                #check vertical
                if row >= 2 and board[row][col] != 0 and board[row][col] == board[row-1][col] == board[row-2][col]:
                    targets.update([(row, col), (row-1, col), (row-2, col)])#update is used for a list of items being added
                    
                #check horizontal
                if col >= 2 and board[row][col] != 0 and board[row][col] == board[row][col-1] == board[row][col-2]:
                    targets.update([(row, col), (row, col-1), (row, col-2)])
                    
        return targets
                
    #crush the items within the coordinates by setting them to 0
    def crush(self, board, targets):
        for row, col in targets:
            board[row][col] = 0
            
    #drop the candies to fill-up the crushed spots
    def drop(self, board):
        #can only drop vertically
        height = len(board)
        width = len(board[0])
        
        #go by each width at a time -> [candy, candy, candy, candy]
        for col in range(width):
            
            #store the candies that won't be crushed
            stack = []
            
            #iterate over height backwards and stack the unmarked
            for row in range(height -1, -1, -1):
                if board[row][col] != 0:
                    stack.append(board[row][col])
            
            #fillers for the cols that didn't get stacked
            fillers = [0] * (height - len(stack))
            
            #add the fillers to stack
            stack += fillers
            
            #create a new col for the board
            row = 0
            while stack:
                item = stack.pop()
                board[row][col] = item
                row += 1
                
        return board