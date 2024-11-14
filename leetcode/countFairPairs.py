class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        fair_pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] >= lower and nums[i] + nums[j] <= upper:
                    fair_pairs.append((i, j))
                continue
        

        return len(fair_pairs)
