class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            required = target - nums[i]

            # check if already seen
            if required in hashmap:
                return [hashmap[required], i]

            # store current number
            hashmap[nums[i]] = i
