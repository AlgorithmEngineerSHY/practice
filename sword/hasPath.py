class Solution:
    def __init__(self):
        self.mat = None
        self.res = False
        self.path = None
        self.len_path = None
        self.rows = None
        self.cols = None
    def hasPath(self, matrix, rows, cols, path):
        if len(matrix) < len(path):
            return False
        if len(path) == 0:
            return True

        new_mat = []
        for i in range(rows):
            tmp_row = []
            for j in range(cols):
                tmp_row.append(matrix[i * cols + j])
            new_mat.append(tmp_row)
        self.mat = new_mat
        self.path = path
        self.len_path = len(path)
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            if self.res == True:
                break
            for j in range(cols):
                self.helper(i, j, set(), 0)
                if self.res == True:
                    break

        return self.res

    def helper(self, row, col, path_set, idx):
        if idx == self.len_path:
            self.res = True
            return None
        if 0 <= row < self.rows and 0 <= col < self.cols and (row, col) not in path_set:
            if self.mat[row][col] == self.path[idx]:
                path_set.add((row, col))
                idx += 1
                self.helper(row + 1, col, path_set, idx)
                self.helper(row, col + 1, path_set, idx)
                self.helper(row - 1, col, path_set, idx)
                self.helper(row, col - 1, path_set, idx)
