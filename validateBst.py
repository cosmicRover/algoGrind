# Problem M 4
# Solution

#O(n) Time | O(d) space because of the recursive call stack

def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
    # if tree is empty, it's a valid bst
    if tree is None:
        return True
    
    # tree.value is the current node's value that gets called recursively
    # first pass will not be triggered (-inf < minValue and maxValue > inf ????)
    if tree.value < minValue or tree.value >= maxValue:
        return False
    
    # calling on left side of the tree with min of -inf and max of current tree's value
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)

    # calling on right side of the tree with min of current tree's value and max of Inf
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)




