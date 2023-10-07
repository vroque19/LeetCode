class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums)//2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)

        return self.merge(left_half, right_half)



    def merge(self, list1: List[int], list2: List[int]) -> List[int]:
        merged = []
        i, j = 0, 0

        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

        if i < len(list1):
            merged.extend(list1[i:])
        merged.extend(list2[j:])

        return merged
