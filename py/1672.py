class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for list in accounts:
            curr = sum(list)
            if max < curr:
                max = curr
        return max