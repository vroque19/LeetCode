class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {} # val:index
        for i, j in enumerate(nums):
            diff = target - j
            if diff in hmap:
                return [hmap[diff], i]
            hmap[j] = i 
        return