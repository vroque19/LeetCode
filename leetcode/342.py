import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log(n, 4) == int(math.log(n, 4))