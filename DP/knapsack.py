
# Problem: DP
# Solution
# Time + Space O(nc) where n is the item length and c is the capacity we explore

def knapsack(items, capacity):

    #init a 2d array with value 0
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]

    for i in range(1, len(items) +1):

        # get the current weight and current value of the item
        currentWeight = items[i-1][1]
        currentValue = items[i - 1][0]

        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i -1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i -1][c], knapsackValues[i -1][c-currentWeight] + currentValue)
    return [knapsackValues[-1][-1], getknapsackItems(knapsackValues, items)]


def getknapsackItems(knapsackValues, items):

    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1

    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i -1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))