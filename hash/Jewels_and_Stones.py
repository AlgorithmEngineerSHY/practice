from collections import Counter
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        c = Counter(S)
        for i in J:
            res += c[i]
        return res