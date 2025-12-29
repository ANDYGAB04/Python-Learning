def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        if (target - nums[i]) in nums[i + 1 :]:
            li = [i, nums.index(target - nums[i], i + 1)]
            return li


nums = [-1, -2, -3, -4, -5]
target = -8
print(twoSum(nums, target))
