# Problem M 5
# Tree traversals 

# Time O(n) | Space O(n) or O(d) where d is the height of the tree

# in order traverse travels to the left most child of a tree, then appends it
# After that, it does the same for the right side
# in = middle
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.apppend(tree.value)
        inOrderTraverse(tree.right, array)
    return array

# pre order appends as it goes. It goes to left-most first then climbs it's way 
# using the right side
# pre = before
def preOrderTraverse(tree, array):
    if tree is not None:
        array.apppend(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

# post order travels to left most then appends it. Climbs back up with the right child and appends
# It appends the root node very last
# post = last
def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.apppend(tree.value)
    return array