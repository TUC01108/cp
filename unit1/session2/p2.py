def goldilocks_approved(nums):
    # newList = nums.sort()
    # justRight = newList[1];
    # if justRight is min(newList) or max(newList):
    #     return -1
    # else:
    #     return justRight
    # pass
    nums.sort()
    if len(nums) < 3:
        return -1
    justRight = nums[1]
    return justRight


nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
