class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        i = len(words) - 1
        return len(words[i])