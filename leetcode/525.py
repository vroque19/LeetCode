class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h_table = {0: -1}
        zeros, ones, longest = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            diff = zeros - ones
            if diff in h_table:
                longest = max(longest, i-h_table[diff])
            else:
                h_table[diff] = i

        return longest
            
