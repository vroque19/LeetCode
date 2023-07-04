class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i, v in enumerate(digits):
            power = len(digits)-1 -i
            num += v*(10**power)
        num+=1
        ret = []
        while num != 0:
            ld = num%10
            ret.append(ld)
            num = num//10
        return ret[::-1]
