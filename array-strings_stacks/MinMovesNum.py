'''
Time O(n) | Space O(1)
formula => abs(num1 - num2) gets you minimum
'''

def minimumMoves(arr1, arr2):
    results = 0

    for x, y in zip(arr1, arr2):
        results += getMin(x, y)

    print(results)
    return results


def getMin(item1, item2):
    item1 = str(item1)
    item2 = str(item2)
    mini = 0

    for x, y in zip(item1, item2):
        result = abs(int(x) - int(y))
        mini += result

    return mini