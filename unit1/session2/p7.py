def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        remainder = num % 3
        if remainder != 0:
            increments_needed = min(remainder, 3 - remainder)
            count += increments_needed
    return count
    

nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))

#understand
# 


#match

#plan

#implement

#review

#evaluate