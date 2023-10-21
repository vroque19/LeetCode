class Solution:
    def maxScore(self, s: str) -> int:
        scores = []
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            scores.append(right.count('1') + left.count('0'))
        return max(scores)
        