def max_sub_array_of_size_k(k, arr):
  '''
  sliding window approach
  start -> k
  '''

  start = 0; sum = 0; maxSum = float("-inf")

  for i in range(len(arr)):
    #add to the sum
    sum += arr[i]

    #slide window when we hit k
    if i >= k-1:
      maxSum = max(maxSum, sum)
      
      #adjust left pointer
      sum -= arr[start]
      start += 1

  return maxSum