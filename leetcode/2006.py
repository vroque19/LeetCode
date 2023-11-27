class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        find the absolute difference of each pair
        iterate over each element i from 0 to len(nums)-2
        for each element j = i+1 to len(nums)-1
        O(n^2)
        we can do better
        iterate over nums from i = 0 to len(nums)-1, subtracting k-nums[i]
        if the absolute difference is found in the tmemo, increment count
        else add it to the tmemo
        """
        tmemo = [nums[0]]
        count = 0
        for i in range(1, len(nums)):
            test1 = nums[i] - k
            test2 = nums[i] + k
            if test1 in tmemo or test2 in tmemo:
                count += tmemo.count(test1)
                count += tmemo.count(test2)
            tmemo.append(nums[i])
        return count


        