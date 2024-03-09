class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        add = 0
        sub = 0
        for i in range(len(nums1)):
            if k == 0 and nums1[i] != nums2[i]:
                return -1
            if nums1[i] == nums2[i]:
                continue
            elif nums1[i] < nums2[i]:
                if (nums2[i] - nums1[i])%k == 0:
                    add += (nums2[i]-nums1[i])/k
                else:
                    return -1
            else:
                if (nums1[i] - nums2[i])%k == 0:
                    sub += (nums1[i]-nums2[i])/k
                    print(sub)
                else:
                    return -1
    
        return int(add) if add == sub else -1
