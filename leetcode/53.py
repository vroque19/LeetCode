class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0] # keep track of max sum over entire array
        max_sum_curr = nums[0] # keep track of max sum up to the current index

        for i in range(1, len(nums)):
            max_sum_curr = max(max_sum_curr+nums[i], nums[i])
            max_sum = max(max_sum, max_sum_curr)

        return max_sum

