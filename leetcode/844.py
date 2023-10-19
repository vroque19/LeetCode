class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for c in s:
            if c in string.punctuation:
                if s1:
                    s1.pop()
                    # print(s1)
                pass
            else:
                s1.append(c)
        for c in t:
            if c in string.punctuation:
                if s2:
                    s2.pop()
                    # print(s2)
                pass
            else:
                s2.append(c)
        # print(s1, "and", s2)
        return s1 == s2