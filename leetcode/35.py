class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for x in nums:
            if int(x) < target:
                i += 1
            else:
                break
        return i