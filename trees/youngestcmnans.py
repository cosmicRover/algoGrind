# Problem M 15
# Solution, non-recursive
# O(d) time where d is the depth pf the tree | O(1) space


# First, figure out the depths of the two nodes
# Second, if depth1 > depth2, backtrack the nodes
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)

    if depthOne > depthTwo:
        return backtrackTheNodes(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackTheNodes(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(descendant, topAncestor):
    depth = 0

    # iterating upwards to the ancestor and incrementing depth
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackTheNodes(firstDescendant, secondDescendant, difference):
    # get the descendant with greater diif backtracked up the tree diff times
    while difference > 0:
        firstDescendant = firstDescendant.ancestor
        difference -= 1
    
    # keep iterating upwards till their descendants are the same
    while firstDescendant != secondDescendant:
        firstDescendant = firstDescendant.ancestor
        secondDescendant = secondDescendant.ancestor
    return firstDescendant
