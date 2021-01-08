class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        backtracking approach. basic -> recrsive
        
        time O(n * 3^L) n is the number of cells on board, L is length of the word to be matched, 3 since 
        this can be seen as a 3-ary tree
        
        space O(L) L is the length of the word that need to be matched
        '''
        height = len(board)
        width = len(board[0])
        for i in range(height):
            for j in range(width):
                if self.backtrack(board, i, j, word, height, width):
                    return True
                
        return False
            
    def backtrack(self, board, row, col, word, height, width):
        #basic step for algorithm to stop
        #here we reduce the word when it letters match hence we expect it to be 0 when we have a complete match
        if len(word) == 0: return True 
        
        #check if we can/should jump into backtracking
        #if the first cell don't match, might as well move to next cell
        if row < 0 or row == height or col < 0 or col == width or board[row][col] != word[0]:
            return False
        
        #recursive step for algorithm to build path and abandon them
        #mark the visited cells so we may compare them on line 22
        board[row][col] = "-1"
        # print(board)
        directions = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
        
        #for each directions of the cell, replace the first index of the word and search
        for x, y in directions:
            if self.backtrack(board, x, y, word[1:], height, width):
                return True
            
        #abandon a path aka revert back the "-1" if not going in suitable direction
        board[row][col] = word[0]
        
        return False