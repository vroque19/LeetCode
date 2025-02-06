class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = Counter(s)
        d2 = Counter(t)

        return d1 == d2
