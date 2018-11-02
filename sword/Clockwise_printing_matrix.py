class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        len_row = len(matrix)
        len_col = len(matrix[0])

        mark = 1
        i_or_j = 'j'
        i, j = 0, 0
        res = []
        while len_row > 0 and len_col > 0:
            if i_or_j == 'j':
                for k in range(len_col):
                    res.append(matrix[i][j])
                    j += mark
                len_row -= 1
                j -= mark
                i += mark
                i_or_j = 'i'
            else:
                for k in range(len_row):
                    res.append(matrix[i][j])
                    i += mark
                len_col -= 1
                i -= mark
                mark *= -1
                j += mark
                i_or_j = 'j'

        return res

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
obj=Solution()
print(obj.printMatrix(a))