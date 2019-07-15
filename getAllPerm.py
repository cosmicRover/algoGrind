# Problem
# Solutions

# constructing new array method
# Time Upper: O(n^2 * n!) | Space O(n*n!)
# Roughly O(n*n!) time | O(n*n!) space

def getPermutations1(array):
    permutations = []
    permutationsHelper1(array, [], permutations)
    return permutations

def permutationsHelper1(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper1(newArray, newPermutation, permutations)

# swapping method
# Time O(n*n!) since perms are N! and each perm has N length
# Space O(n*n!)

def getPermutations2(array):
    permutations = []
    permutationsHelper2(0, array, permutations)
    return permutations

def permutationsHelper2(i, array, permutations):
    if  i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):

            # no swapping in the first loop since i == 1
            swap(array, i, j) # [1, 2, ...] -> # [2, 1, ...]
            permutationsHelper2(i + 1, array, permutations)
            swap(array, i, j) # [2, 1, ...] -> [1, 2, ...]

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
