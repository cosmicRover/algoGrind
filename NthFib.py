# Problem E5
# Soultions


# O(2^n) | O(n) space
# use recursion to get the nth fib


def nthFib(target):

    if target == 2:
        return 1
    elif target == 1:
        return 0
    else:
        return nthFib(target - 1) + nthFib(target - 2)

# O(n) time | O(n) space
# use a hash table to store fibs and return them


def storedFib(n, table={2: 1, 1: 0}):

    if n in table:
        return table[n]
    else:
        table[n] = storedFib(n - 1, table) + storedFib(n - 2, table)
        return table[n]


# O(n) time | O(1) space
# use an array, a counter to iterate through the fib values and return the 2nd element
# edge case is when target is < 0

def caclFib(target):

    arr = [0, 1]
    counter = 3

    while counter <= target:
        fib = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = fib
        counter += 1
    return arr[1] if target > 1 else arr[0]
