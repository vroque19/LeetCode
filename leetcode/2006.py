class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        |nums[i]-nums[j]| == k
        
        nums[i] == nums[j] - k
        nums[i] == nums[j] + k
        """
        hmap = {}
        count = 0

        for j in nums:
            test1 = j + k
            test2 = j - k
            if test1 in hmap:
                count += hmap[test1]
            if test2 in hmap:
                count += hmap[test2]
            hmap[j] = hmap.get(j, 0) + 1
        return count