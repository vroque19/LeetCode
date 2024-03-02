class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        new_s = ""
        zeros_count = s.count('0')
        ones_count = s.count('1')
        while zeros_count > 0 or ones_count > 1:
            if  ones_count > 1:
                new_s += '1'
                ones_count -= 1
            else:
                new_s += '0'
                zeros_count -= 1
        new_s += '1'
        return new_s

        