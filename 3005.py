from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        tot_freq = 0
        max_freq = 0
        my_map = Counter(nums)
        for k, v in my_map.items():
            if v > max_freq:
                max_freq = v
                tot_freq = max_freq
            elif v == max_freq:
                tot_freq += v
            else:
                continue

        return tot_freq
