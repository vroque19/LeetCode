class Solution:
    def maxScore(self, s: str) -> int:
        right_score = s.count('1')
        max_score = 0
        left_score = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                # a '0' is moved to the left half
                left_score += 1
            else:
                # a '1' is moved to the left half
                right_score -= 1
            max_score = max(max_score, left_score + right_score) # max of max_score and tot curr score
        return max_score
    # time complexity: O(n) 