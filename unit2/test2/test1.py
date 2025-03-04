def two_sum(nums, target):
    sumDict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in sumDict:
            return [sumDict[complement], i]
        sumDict[num] = i
    
#Input: 
nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))
#Output: [0,1]
#Example 2:
#Input: nums = [3,2,4], target = 6
nums = [3,2,4]
target = 6
print(two_sum(nums, target))
#Output: [1,2]