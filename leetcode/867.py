class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_mat = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                new_mat[c][r] = matrix[r][c]
        return new_mat
