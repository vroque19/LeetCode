class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        0 1 1 2 3 5 8 13 21 34
        """
        i = 0
        j = 1
        count = 0
        
        while count != n:
            j = i+j
            i = j-i
            count+=1
        return i