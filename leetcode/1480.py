class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = []
        i = 0
        num = 0
        while i < len(nums):
            num+=nums[i]
            run_sum.append(num)
            i+=1
        return run_sum