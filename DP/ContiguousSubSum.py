'''
Contiguous: Is a sequence of items without breaks
i.e. given [2, 1, 5, 6, 7]
contiguous sub array can be [2, 1, 5]... etc
'''

'''
Given an array of ints, find the max contiguous sub array sum
The sub-problem in this context is to figure out:
-> are you better off having the sum of the elements from arr[:i]
or 
-> or adding the ith value arr[i] to dp[i-1] for a better sum.

Time O(n) | Space O(n) due to sp array although can be done in constant space
by only memoizing the last max
'''

def solve(arr):
    dp = [0] * len(arr)

    #the sub problem is to fi
    for i in range(len(arr)):
        if i == 0:
            dp[i] = arr[i]
        else:
            dp[i] = max(dp[i], dp[i-1] + arr[i])

    print(dp)
    return max(dp)


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solve(arr))