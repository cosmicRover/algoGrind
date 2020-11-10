def length_of_longest_substring(arr, k):
  '''
  sliding window start -> end
  Same approach as longest substring of same letters with repalcemet
  Time O(n) | Space O(1) due to dic being max of size 2
  '''
  start = 0; longest = 0; maxLength = 0;
  dic = {}

  for end in range(len(arr)):
    #save frequency
    char = arr[end]
    if char not in dic:
      dic[char] = 0
    dic[char] += 1

    #save longest 1
    if arr[end] == 1:
      longest = max(longest, dic[1])

    #slide the window
    size = end-start + 1
    if size - longest > k:
      char = arr[start]
      dic[char] -= 1
      start += 1

    #save the max length
    maxLength = max(maxLength, end-start+1)

  return maxLength















