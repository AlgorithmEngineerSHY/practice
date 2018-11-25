class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        n_zs = [s.count('0') for s in strs]
        n_z_o = [(n_zs[x], len(strs[x]) - n_zs[x]) for x in range(len(strs))]
        for n_z, n_o in n_z_o:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if n_z <= i and n_o <= j:
                        dp[i][j] = max(dp[i][j], dp[i - n_z][j - n_o] + 1)
        return dp[m][n]