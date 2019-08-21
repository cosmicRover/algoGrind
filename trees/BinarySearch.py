# Problem E6
# Solutions

# Recursive
# O(log(n)) time | space O(log(n)) since recursive calls add to the stack
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    # base case, target not found
    if left > right:
        return -1

    # calculate the middle index and round down. Cuts array in half
    middle = (left + right) // 2
    # gets the value associated with middle index for comparison
    potentialMatch = array[middle]

    # if found
    if target is potentialMatch:
        return middle
    # if it is less than target
    elif target < potentialMatch:
        binarySearchHelper(array, target, left, middle - 1)
    # if its more
    else:
        return binarySearchHelper(array, target, middle + 1, right)

# Iterative.
# O(log(n)) time | space O(1)
# Same as before but wrap the whole thing with in a while loop
# and increment/decrement right/left pointers accordingly

def binarySearchHelperIterative(array, target, left, right):

    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]

        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1