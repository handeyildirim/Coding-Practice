# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
# so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  if nums:
    sum = 0
    if 13 in nums:
      # if array does not contain 13
      idx_thirteen = nums.index(13)
      len_nums = len(nums)
      if len_nums-1 == idx_thirteen:
        nums.pop(idx_thirteen)
      else:
        nums.pop(idx_thirteen)
        nums.pop(idx_thirteen)
        if 13 in nums:
          sum13(nums)
    for i in nums:
        sum = i + sum
    return sum
  else:
    return 0

# sum13([1, 2, 2, 1]) → 6	6	OK	
# sum13([1, 1]) → 2	2	OK	
# sum13([1, 2, 2, 1, 13]) → 6	6	OK	
# sum13([1, 2, 13, 2, 1, 13]) → 4	4	OK	
# sum13([13, 1, 2, 13, 2, 1, 13]) → 3	3	OK	
# sum13([]) → 0	0	OK	
# sum13([13]) → 0	0	OK	
# sum13([13, 13]) → 0	0	OK	
# sum13([13, 0, 13]) → 0	0	OK	
# sum13([13, 1, 13]) → 0	0	OK	
# sum13([5, 7, 2]) → 14	14	OK	
# sum13([5, 13, 2]) → 5	5	OK	
# sum13([0]) → 0	0	OK	
# sum13([13, 0]) → 0
