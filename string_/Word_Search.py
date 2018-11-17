class Solution:
    def __init__(self):
        self.board = None
        self.word = None
        self.res = False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                self.helper(row, col, 0, len(word), set())

        return self.res

    def helper(self, i, j, idx, rest, pass_set):
        if self.res == True:
            return None

        if self.board[i][j] == self.word[idx]:
            rest -= 1
            if rest == 0:
                self.res = True
                return None
            tmp_set = pass_set.union(set([(i, j)]))
            if j > 0 and (i, j - 1) not in tmp_set:
                self.helper(i, j - 1, idx + 1, rest, tmp_set)
            if j < len(self.board[0]) - 1 and (i, j + 1) not in tmp_set:
                self.helper(i, j + 1, idx + 1, rest, tmp_set)
            if i > 0 and (i - 1, j) not in tmp_set:
                self.helper(i - 1, j, idx + 1, rest, tmp_set)
            if i < len(self.board) - 1 and (i + 1, j) not in tmp_set:
                self.helper(i + 1, j, idx + 1, rest, tmp_set)




obj = Solution()
print(obj.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "SEE"))