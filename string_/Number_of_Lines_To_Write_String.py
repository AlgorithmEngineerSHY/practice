class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        w_list = [widths[ord(x) - 97] for x in S]
        row, col = 1, 0

        for i in w_list:
            col += i
            if col == 100:
                col = 0
                row += 1
            elif col > 100:
                col = i
                row += 1
        return [row, col]