class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = 0
        tokens = sorted(tokens)
        l = 0
        r = len(tokens)-1
        score = 0
        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                l += 1
                max_score = max(max_score, score)
            elif 1 <= score:
                power += tokens[r]
                score -= 1
                r -= 1
                max_score = max(max_score, score)
            else:
                break
        return max_score
