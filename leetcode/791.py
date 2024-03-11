class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cntr = Counter(s)
        new = ""
        for i in range(len(order)):
            c = order[i]
            if c in s:
                new+=c*cntr[c]
                cntr[c] -= cntr[c]
            else:
                continue
        for k, v in cntr.items():
            while v > 0:
                new += k
                v -= 1
            continue

        return new
        