class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    # find the max of each column and store it in a dict as col:num
    # go through each row and update the dict
    # if row_min in col_max -> lucky number
        dict_max = self.get_max_in_each_col(matrix)
        lucky_numbers = []
        for i in range(len(matrix)):
            curr_min = min(matrix[i])
            idx = matrix[i].index(curr_min)
            # print(idx, curr_min)
            if dict_max[idx] == curr_min:
                lucky_numbers.append(curr_min)
        return lucky_numbers

        
    def get_max_in_each_col(self, matrix):
        dict_max = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = matrix[i][j]
                if j not in dict_max:
                    dict_max[j] = curr
                    # print("i not in dict")
                    pass
                if curr > dict_max[j]:
                    dict_max[j] = curr
        return dict_max



        