def countTriplets(arr, n, sum): 
  
  '''
  Two pointer left -> right
  Similar to 3sum, it will take O(n^2)
  '''
  count = 0
  
  for i in range(n-2):
    left = i+1
    right = n-1
    
    while left < right:
      s = arr[i]+arr[left]+arr[right]
      
      if s < sum:
        count += 1
        
      right -= 1
      
      if left == right:
        left = left+1
        right = n-1
  return count