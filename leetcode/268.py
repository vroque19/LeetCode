class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        an = n+1
        a0 = 0
        summ = (n/2)*(a0+an)
        return int(summ - sum(nums))
        
        