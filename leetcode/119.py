class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        prev_row = [1]
        for i in range(1, rowIndex+1):
            row = [1]
            for j in range(1, i):
                row.append(prev_row[j-1]+prev_row[j])
            row.append(1)
            prev_row = row
            print(row)
        return row



        """
        :type rowIndex: int
        :rtype: List[int]
        """
