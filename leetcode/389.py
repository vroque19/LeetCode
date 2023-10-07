class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum_s = 0
        sum_t = 0

        for x in s:
            sum_s += ord(x)
        for x in t:
            sum_t += ord(x)

        letter = sum_t - sum_s

        return chr(letter)