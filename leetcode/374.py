# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        if n == 1:
            return n
        while lo <= hi:
            curr_guess = (hi + lo) // 2
            if guess(curr_guess) == -1:
                hi = curr_guess - 1
            elif guess(curr_guess) == 1:
                lo = curr_guess + 1
            elif guess(curr_guess) == 0:
                return curr_guess
            
        