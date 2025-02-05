def two_sum(nums: list[int], target: int) -> tuple:
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            return (hash_map[complement], i)
        hash_map[nums[i]] = i
    return


"""
target = 3
"""
nums = [1, 3, 6, 5, 2]

res = two_sum(nums, 3)

print(res)
