'''
Sliding window approach. We keep a running sum and check to see if sum >= s
If sum >= s, then we get the length of subarray with end-start.
We calculate length insid the while loop since we need to readjust for sum to be < s

Time O(n) | Space O(1)
'''


def smallest_subarray_with_given_sum(s, arr):
  start = 0; sum = 0;
  minLen = float("inf")

  for end in range(len(arr)):
    #keep a sum
    sum += arr[end]

    #if sum >= s, we jump inside a loop and keep calculating the length of the sub 
    #while incrementing start and substartcting start from the sum
    if sum >= s:
      while sum >= s:
        minLen = min(minLen, end-start+1)
        sum -= arr[start]
        start += 1

  return minLen if minLen != float("inf") else -1