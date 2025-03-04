# Complete the 'contains_duplicate' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY nums as parameter.
def contains_duplicate(nums):
    setDups = set()
    for num in nums:
        if num in setDups:
            return True
        setDups.add(num)
    return False


#Example 1:
nums = [1,2,3,1]
print(contains_duplicate(nums))
#Output: True

#Example 2:
#Input: nums = [1,2,3,4]
#Output: False

#Example 3:
#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: True