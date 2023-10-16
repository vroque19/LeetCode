class Solution(object):
    def generate(self, numRows):
        res = [[1]for y in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                res[i].append(res[i-1][j]+res[i-1][j-1])
                # print(i, "add", res[i-1][j], "and",res[i-1][j-1],"to get", res[i][j])
            res[i].append(1)
        return res
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        