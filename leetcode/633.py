class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for i in range(int(sqrt(c))+1):

            diff = c - pow(i, 2)
            print(diff)
            if sqrt(diff).is_integer():
                return True
        return False
