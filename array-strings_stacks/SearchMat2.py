class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == [[]]:
            return False

        for row in matrix:
            if target < row[0] or target > row[len(row) - 1]:
                continue

            else:
                #decide what side to search based on the midpoint
                mid = len(row) // 2

                if target <= row[mid]:
                    for x in row[:mid]:
                        if target == x:
                            return True

                if target >= row[mid]:
                    for x in row[mid:]:
                        if target == x:
                            return True

        else:
            return False
