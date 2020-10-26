'''
Time O(n) | Space O(len(str))
'''

def longest_substring_with_k_distinct(str, k):
  '''
  Sliding window approach. start and end of a window to keep tarck of valid characters
  '''

  count = {}
  start = 0; maxLen = 0;

  for end in range(len(str)):
    
    #build up the frequency as you go
    char = str[end]
    if char not in count: #init if dont exist
      count[char] = 0
    count[char] += 1

    #slide the window while length > k
    while len(count) > k:
      char = str[start]
      
      #decrease the frequencies in the hopes that we can eventually delete them
      count[char] -= 1
      if count[char] == 0:
        del count[char]
      
      #slide the start pointer to the right to indicate that we have moved on
      start += 1

    maxLen = max(maxLen, end-start+1)

  return maxLen