class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        n_L = moves.count('L')
        n_R = moves.count('R')
        n_U = moves.count('U')
        n_D = moves.count('D')
        return n_L == n_R and n_U == n_D