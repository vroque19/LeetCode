class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [abs(x) for x in nums]
        sorted_list = sorted(nums)
        for i in range(len(sorted_list)):
            sorted_list[i] = sorted_list[i] ** 2
        return sorted_list
