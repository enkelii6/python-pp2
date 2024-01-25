def has33(nums):
    for i in nums:
        if nums[i+1] == nums[i] and nums[i] == 3:
            return True
    return False
print(has33(list(map(int, input().split()))))
