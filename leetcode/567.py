import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        fmap1 = dict.fromkeys(string.ascii_lowercase, 0)
        fmap2 = dict.fromkeys(string.ascii_lowercase, 0)

        for i in range(len(s1)):
            fmap1[s1[i]] += 1
            fmap2[s2[i]] += 1
        
        matches = 0
        for key, val in fmap1.items():
            if fmap1[key] == fmap2[key]:
                matches += 1
            continue
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            fmap2[s2[r]] += 1
            if fmap1[s2[r]] == fmap2[s2[r]]:
                matches += 1
            elif fmap1[s2[r]] +1 == fmap2[s2[r]]:
                matches -=1
            
            fmap2[s2[l]] -= 1
            if fmap1[s2[l]] == fmap2[s2[l]]:
                matches += 1
            elif fmap1[s2[l]] -1 == fmap2[s2[l]]:
                matches -=1         
            l += 1

        return matches == 26
