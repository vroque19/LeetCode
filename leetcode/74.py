class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m = len(matrix)
        n = len(matrix[0])
        h = m - 1
        if m == 1 and n == 1:
            if target == matrix[0][0]:
                return True
            else:
                return False
        while l<=h:
            target_row = (l+h)//2
            if target < matrix[target_row][0]:
                h = target_row -1
            elif target > matrix[target_row][-1]:
                l = target_row + 1
            else:
                break
        l = 0
        h = n - 1

        while l <= h:
            mid = (l+h)//2
            if target < matrix[target_row][mid]:
                h = mid - 1
            elif target > matrix[target_row][mid]:
                l = mid + 1
            else:
                return True
        return False
