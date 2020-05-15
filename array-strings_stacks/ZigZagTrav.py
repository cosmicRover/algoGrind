'''
Given a 2d array of n elements, return a single list of n elements after traversing the 2d array in a zig-zag manner.
The key takeaway from this problem is to think about how to traverse the tree on the top right and bottom left corners.
You need to be careful while traversing, writing down the steps and special cases for traversing is highly advised 
'''

def zzTraverse(array):
    #get the height and width of the matrix and -1 from it since we will use it to traverse
    height = len(array) - 1
    width = len(array[0]) - 1

    result = []
    row = col = 0 #starting point of our traversal is 0,0

    goingDown = True #a bool to indicate direction of traversal

    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        if goingDown:
            #formula to traverse for left-bottom, hence we can't go down
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1

        else:
            # if not going down, we go top right
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1

            else:
                row -= 1
                col += 1

    return result

# just checks if we are out of bounds by comparing row and col with height and width
def isOutOfBounds(row, col, height, width):
    return True if row < 0 or row > height or col < 0 or col > width else False


inputArr = [
    [1,3,4,10],
    [2,5,9,11],
    [6,8,12,15],
    [7,13,14,16],
]

print(zzTraverse(inputArr))