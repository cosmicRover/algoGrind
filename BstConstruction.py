# Problem M3
# Solution

# Average: O(log(N)) time | O(1) space -> recursive solution takes O(N) sapce
# Worst: O(N) time | O(1) space

class BST:

    # init value with left/right
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    # returns the left-most value of a BST. In this case, it's the smallest
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    # insert a node based on it being > or < currentNode
    # find a None Node and insert it there
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode > currentNode.value:
                    if currentNode.right is None:
                        currentNode.right = BST(value)
                        break
                    else:
                        currentNode = currentNode.right
        return self

    # look for a node iteratively and return True
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    # removes a node. First itteratively look for it on the tree
    def remove(self, value, parentNode = None):
        currentNode = self

        while currentNode is not None:
            
            # continue to iterate till we find the node
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            
            else: # found the node here
                
                # the node has left and right leaves, currentNode becomes the min of currentNode's right
                # then remove the right node
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                
                # if no parentNode
                elif parentNode is None:
                    
                    # if left exists, do a re-shuffle. currentNode becomes currentNode's left
                    # currentNode's right becomes currentNode's left's right
                    # currentNode's left becomes currentNode's left's left
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left

                    # if right exists, do a re-shuffle. currentNode becomes currentNode's right
                    # currentNode's left becomes currentNode's right's right
                    # currentNode's right becomes currentNode's right's right
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    
                    # if there's only one node in the BST. just set it to none
                    else:
                        currentNode.value = None

                # if the node is a left leaf, set parent to left if left is not null. else set it to right
                elif currentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                
                # same as before for if it's a right leaf
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self