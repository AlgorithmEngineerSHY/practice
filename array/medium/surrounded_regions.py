'''
Given a 2D board containing'X'and'O', capture all regions surrounded by'X'.
A region is captured by flipping all'O's into'X's in that surrounded region .
'''
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        m, n = len(board), len(board[0])
        save = [ij for k in range(m + n) for ij in ((0, k), (k, 0), (m - 1, k), (k, n - 1))]
        while save:
            i, j = save.pop()
            if 0 <= i <= m - 1 and 0 <= j <= n - 1 and board[i][j] == 'O':
                board[i][j] = 'S'
                save += ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j))
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
