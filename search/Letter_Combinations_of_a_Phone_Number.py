class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        letter_dict = {'2': ['a', 'b', 'c'],
                       '3': ['d', 'e', 'f'],
                       '4': ['g', 'h', 'i'],
                       '5': ['j', 'k', 'l'],
                       '6': ['m', 'n', 'o'],
                       '7': ['p', 'q', 'r', 's'],
                       '8': ['t', 'u', 'v'],
                       '9': ['w', 'x', 'y', 'z']}

        pre = letter_dict[digits[0]]

        for i in digits[1:]:
            cur = letter_dict[i]
            pre = self.helper(pre, cur)

        return pre
    def helper(self, x, y):
        len_x = len(x)
        len_y = len(y)
        res = []
        for i in range(len_x):
            for j in range(len_y):
                res.append(x[i] + y[j])
        return res




obj= Solution()
print(obj.letterCombinations('234'))



