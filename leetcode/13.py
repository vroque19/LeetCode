class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result = 0
        prev_value = 0

        for i in range(len(s) - 1, -1, -1):
            value = numerals[s[i]]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        print(result)
        return result