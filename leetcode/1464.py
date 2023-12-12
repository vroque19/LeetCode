class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        my_map = dict()
        my_map = self.mapData(nums, my_map)
        temp = nums
        nums = sorted(nums)
        print(nums, temp)
        num1 = nums[len(nums)-2]
        num2 = nums[len(nums)-1]
        temp1 = temp[my_map[num1]]
        temp2 = temp[my_map[num2]]
        
        return (temp1-1)*(temp2-1)

    def mapData(self, nums, my_map):
        for i in range(len(nums)):
            my_map[nums[i]] = i
        return my_map