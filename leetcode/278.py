# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        if n == 1:
            return 1
        while lo <= hi:
            mid = (lo + hi)//2
            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
    