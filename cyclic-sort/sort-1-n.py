def cyclic_sort(nums):
  '''
  cycle sort with unique numbers from 1 to n. Only works with unique numbers from 1 to n
  keep swapping until a number is at it's proper position. 

  Since nums start from 1 rather than 0, index need to be substracted by 1

  time O(n)
  '''

  i = 0

  while i < len(nums):
    #the index where the number is supposed to be
    index = nums[i]-1

    #keep swapping until the number is at it's proper index
    if nums[i] != nums[index]:
      nums[i], nums[index] = nums[index], nums[i] 
    
    #otherwise proceed to the enxt element
    else:
      i += 1
  
  return nums