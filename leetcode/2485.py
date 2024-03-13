class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        for i in range(n):
            sum_left = 0
            sum_right = 0
            for j in range(i+1):
                sum_left += j
            for k in range(i, n+1):
                sum_right += k
            if sum_left == sum_right:
                return i
        return -1
