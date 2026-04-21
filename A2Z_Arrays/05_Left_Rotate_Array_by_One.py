def left_rotate_by_one(nums):
    if len(nums) == 0:
        return nums

    first = nums[0]

    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]

    nums[-1] = first
    return nums
