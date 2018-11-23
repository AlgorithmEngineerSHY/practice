class Solution:
    def __init__(self):
        self.n_row = None
        self.n_col = None
        self.board = None

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        '''
        1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡
        2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活
        3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡
        4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活'''
        '''
        状态0： 死细胞转为死细胞
        状态1： 活细胞转为活细胞
        状态2： 活细胞转为死细胞
        状态3： 死细胞转为活细胞'''
        self.n_row = len(board)
        self.n_col = len(board[0])
        self.board = board
        for row in range(self.n_row):
            for col in range(self.n_col):
                self.board[row][col] = self.helper(row, col)
                print(self.board[row][col], row, col)
        for row in range(self.n_row):
            for col in range(self.n_col):
                self.board[row][col] %= 2
    def helper(self, row, col):
        num_alive = 0
        if row - 1 >= 0 and col - 1 >= 0:
            num_alive += self.nmsl(row - 1, col - 1)
        if row - 1 >= 0:
            num_alive += self.nmsl(row - 1, col)
        if row - 1 >= 0 and col + 1 < self.n_col:
            num_alive += self.nmsl(row - 1, col + 1)
        if col + 1 < self.n_col:
            num_alive += self.nmsl(row, col + 1)
        if row + 1 < self.n_row and col + 1 < self.n_col:
            num_alive += self.nmsl(row + 1, col + 1)
        if row + 1 < self.n_row:
            num_alive += self.nmsl(row + 1, col)
        if row + 1 < self.n_row and col - 1 >= 0:
            num_alive += self.nmsl(row + 1, col - 1)
        if col - 1 >= 0:
            num_alive += self.nmsl(row, col - 1)
        state = self.board[row][col]
        if state == 0:
            if num_alive == 3:
                return 3
            else:
                return 0
        else:
            if num_alive < 2:
                return 2
            elif 2 <= num_alive <= 3:
                return 1
            else:
                return 2
    def nmsl(self, i, j):
        state = self.board[i][j]
        if state == 0 or state == 3:
            return 0
        else:
            return 1


obj = Solution()
obj.gameOfLife([[0,1,0],
                [0,0,1],
                [1,1,1],
                [0,0,0]])