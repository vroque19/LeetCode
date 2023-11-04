class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        for i in range(len(left)):
            curr_time = abs(0-left[i])
            ans = max(ans, curr_time)
        for i in range(len(right)):
            curr_time = abs(n-right[i])
            ans = max(ans, curr_time)

        return ans
