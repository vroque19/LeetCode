class Solution:
    def sortVowels(self, s: str) -> str:
        # a e i o u
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_upper = ['A', 'E', 'I', 'O', 'U']
        s_vowels = []
        new_s = ""
        j = 0
        for i in range(len(s)):
            if s[i] in vowels or s[i] in vowels_upper:
                s_vowels.append(s[i])
                print(ord(s[i]))
        s_vowels = sorted(s_vowels)
        print(s_vowels)
        
        for i in range(len(s)):
            if s[i] in vowels or s[i] in vowels_upper:
                new_s += s_vowels[j]
                j += 1
                continue
            new_s += (s[i])
        
        return new_s