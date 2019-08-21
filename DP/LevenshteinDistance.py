class Solution(object):

    # Time O(n*m) where n and m is the length of the two words
    # Space O(n*m) just as described before

    # A more optimal space soultion would be to only store the current and previous row on the table using dp
    # check this: https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition for some excellent explantion

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # init the 2d array with width of len(second_word) + 1 and height of len(first_word) + 1
        # and we also put [0, 1, 2, 3 ... len(second_word) + 1 ] on each row
        table = [[x for x in range(len(word2) + 1)]
                 for y in range(len(word1) + 1)]

        print("init table", table)

        """
        we then add another [0, 1, 2, 3 ...] to the first elements on the rows so it looks like:
        
        [
        [0, 1, 2, 3]
        [1, 1, 2, 3]
        [2, 1, 2, 3]
        [3, 1, 2, 3]
        ]
        
        """
        for i in range(len(table)):
            table[i][0] = i

        print("table after adding all the initial values", table)

        # using a double for loop, we check the columns and the rows
        # row has a length of first_word +1 and column and length of second_word + 1 for the row
        # we start at index 1 for both
        for column in range(1, len(word1) + 1):

            for row in range(1, len(word2) + 1):

                # if the word1's letter we are comparing matches with word2's letter
                # we copy the value from it's top left diagonal into the current table[column][row] cell
                if word1[column - 1] == word2[row - 1]:
                    table[column][row] = table[column - 1][row - 1]

                # otherwise, our current cell gets the minimum of the previous cell, top cell, and top left diagonal cell
                else:
                    table[column][row] = 1 + min(table[column][row - 1],
                                                 table[column - 1][row], table[column - 1][row - 1])

        print("final table ", table)

        # we return the very last cell of the table
        return table[-1][-1]
