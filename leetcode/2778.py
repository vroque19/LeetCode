class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        for i in range(1, len(nums)+1):
            if len(nums) % i == 0:
                n = nums[i-1]
                sum = sum + (n**2)
        return sum
        

        # time: O(n)
        # space: O(1)