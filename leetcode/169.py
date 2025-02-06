class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        res, count = 0, 0
        for k, v in d.items():
            if d[k] > count:
                count = d[k]
                res = k
        return res
