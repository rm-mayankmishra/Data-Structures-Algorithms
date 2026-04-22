def linear_search(nums, target):
    for i in nums:
        if nums[i] == target:
            return i
    return -1
