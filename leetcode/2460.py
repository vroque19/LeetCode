class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        if nums[i] == nums[i+1]: nums[i] = 2*nums[i] and nums[i+1]==0
        else: skip
        move all zeros to the end
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
            continue
        cnt = nums.count(0)
        zeros=[0 for _ in range(cnt)]
        while cnt != 0:
            nums.remove(0)
            cnt = cnt - 1
        nums += zeros
        return nums