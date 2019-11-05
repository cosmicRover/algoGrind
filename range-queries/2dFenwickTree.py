# Fenwick tree can be used to calculate range queries in multiple dimensions.
# step1: build the BIT stpe2: implement ways to sum corners e.g. sumCroner() step3: implement way to update BIT e.g. update()

class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix: return
        self.M, self.N = len(matrix), len(matrix[0]) #get the height and width of the input matrix
        
        self.mat  = [[0] * self.N for _ in range(self.M)] #declare a new matrix of given height/width since input is immutable
        self.BIT  = [[0] * (self.N + 1) for _ in range(self.M + 1)] #the binary indexed tree with +1 to height and width
        
        self.buildTree(matrix)

    #builds the initial tree from the original values 
    def buildTree(self, matrix):
        for i in range(self.M):
            for j in range(self.N):
                self.update(i, j, matrix[i][j])

    #method to update the sums
    def update(self, row, col, val):
        diff  = val - self.mat[row][col] #get diff between new val and previous 
        
        treeRow, self.mat[row][col] = row + 1, val #set tree row upto the BIT size and the new val to mat[row][column]
        
        # a loop to update the matrix with new values upward
        while treeRow <= self.M:
            treeCol = col + 1
            while treeCol <= self.N:
                self.BIT[treeRow][treeCol] += diff
                treeCol += (treeCol & -treeCol)
            treeRow += (treeRow & -treeRow)

    #sumRegion gets sums of 4 corners from a rectangle. (row2, col2) + (row1-1, col1-1) - (row1 -1, col2) - (row2, col1 -1)
    def sumRegion(self, row1, col1, row2, col2):
        return self.sumCorner(row2, col2)         + \
               self.sumCorner(row1 - 1, col1 - 1) - \
               self.sumCorner(row1 - 1, col2)     - \
               self.sumCorner(row2, col1 - 1)

    #gets the sum of a corner from a rectangle
    def sumCorner(self, row, col):
        res, i = 0, row + 1
        while i:
            j = col + 1
            while j:
                res += self.BIT[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res