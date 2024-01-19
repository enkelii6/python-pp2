def has33(nums):
    a = False
    for i in nums:
        if nums[i] == nums[i-1] and nums[i] == 3:
            a = True
            break
    print(a)
    return a
lst = list(map(int, input().split()))
has33(lst)