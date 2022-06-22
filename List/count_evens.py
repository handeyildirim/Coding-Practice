# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

# Expected	Run		
# count_evens([2, 1, 2, 3, 4]) → 3	3	OK	
# count_evens([2, 2, 0]) → 3	3	OK	
# count_evens([1, 3, 5]) → 0	0	OK	
# count_evens([]) → 0	0	OK	
# count_evens([11, 9, 0, 1]) → 1	1	OK	
# count_evens([2, 11, 9, 0]) → 2	2	OK	
# count_evens([2]) → 1	1	OK	
# count_evens([2, 5, 12]) → 2	2	OK	
# other tests
# OK

def count_evens(nums):
  if not nums:
    return 0
  else:
    count = 0
    for i in nums:
      if i%2 == 0:
        count += 1
    return count
  
# You can see another solution as an alternative below.

def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count = count + 1
  return count
