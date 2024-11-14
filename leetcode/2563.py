class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bin(l, r, pivot_val):
            while l <= r:
                mid = (l+r)//2
                if pivot_val >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (bin(i+1, len(nums)-1, up) - bin(i+1, len(nums)-1, low-1))
        
        return res
