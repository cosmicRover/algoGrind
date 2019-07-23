# Problem M 19
# Solution

# Time O(n*2^n) | Space O(n*2^n)

def powerset(inputArray):
    subsets = [[]]

    # iterate through the inputArray and the subsets
    # append current element along with the current subset
    for element in inputArray:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [element])
    return subsets

input = [1, 2, 3]
print(powerset(input))