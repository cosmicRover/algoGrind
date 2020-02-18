class Solution:
    def countNegatives(self, grid: [[int]]) -> int:
        count = 0
        
        for x in grid:
            for y in reversed(x):
                if y >0: break #return early if encountered non-negative numbers
                if y <0:
                    count += 1
        return count