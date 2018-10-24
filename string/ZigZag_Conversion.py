class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        len_s = len(s)
        if len_s <= numRows or len_s <= 1 or numRows == 1:
            return s
        result = ''
        helper = [''] * numRows

        for i in range(len_s):
            idx = i % (numRows * 2 - 2)
            if idx < numRows:
                helper[idx] += s[i]
            else:
                idx = numRows * 2 - 2 - idx
                helper[idx] += s[i]
        for string in helper:
            result += string
        return result

