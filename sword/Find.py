class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        col = len(array[0])
        init_row = row - 1
        init_col = 0
        while init_row >= 0 and init_col < col:
            x = array[init_row][init_col]
            if x == target:
                return True
            elif x > target:
                init_row -= 1
            else:
                init_col += 1
        return False