'''
Time O(n) | Space O(1)
'''

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        #find the rook
        rook = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                    rook = (i,j)
                    break
                    
        height = len(board)
        width = len(board[0])
        cap = 0
        
        #check four directions for avialble capture
        #right
        move = rook[1]
        while move < width:
            if board[rook[0]][move] == "B": break
            if board[rook[0]][move] == "p": 
                cap += 1
                break
            move += 1
        
        #up
        move = rook[0]
        while move > -1:
            if board[move][rook[1]] == "B": break
            if board[move][rook[1]] == "p": 
                cap += 1
                break
            move -= 1
        
        #left
        move = rook[1]
        while move > -1:
            if board[rook[0]][move] == "B": break
            if board[rook[0]][move] == "p": 
                cap += 1
                break
            move -= 1
            
        #down
        move = rook[0]
        while move < height:
            if board[move][rook[1]] == "B": break
            if board[move][rook[1]] == "p": 
                cap += 1
                break
            move += 1
        
        return cap