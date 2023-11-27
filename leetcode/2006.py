class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        memo = [nums[0]]
        count = 0
        for i in range(1, len(nums)):
            test1 = nums[i] - k
            test2 = nums[i] + k
            if test1 in memo or test2 in memo:
                count += memo.count(test1)
                count += memo.count(test2)
            memo.append(nums[i])
        return count


        