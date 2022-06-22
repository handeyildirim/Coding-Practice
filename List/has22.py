# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# Expected	Run		
# has22([1, 2, 2]) → True	True	OK	
# has22([1, 2, 1, 2]) → False	False	OK	
# has22([2, 1, 2]) → False	False	OK	
# has22([2, 2, 1, 2]) → True	True	OK	
# has22([1, 3, 2]) → False	False	OK	
# has22([1, 3, 2, 2]) → True	True	OK	
# has22([2, 3, 2, 2]) → True	True	OK	
# has22([4, 2, 4, 2, 2, 5]) → True	True	OK	
# has22([1, 2]) → False	False	OK	
# has22([2, 2]) → True	True	OK	
# has22([2]) → False	False	OK	
# has22([]) → False	False	OK	
# has22([3, 3, 2, 2]) → True	True	OK	
# has22([5, 2, 5, 2]) → False	False	OK	
# other tests
# OK

def has22(nums):
  if 2 not in nums:
    return False
  else:
    tut = False
    for i in range(len(nums)):
      if i != 0:
        if nums[i] == 2 and nums[i-1] == nums[i]:
          return True
    return False
