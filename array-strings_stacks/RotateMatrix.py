'''
The trick here is to realize that a 90 degree rotation is basically
an upside down reversal folloed by a reversal of the rows and columns
Time O(n^2) | Space O(1)
'''

class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        matrix.reverse()
        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]