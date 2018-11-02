class Solution:
    def StrToInt(self, s):
        try:
            return int(s)
        except Exception as e:
            return 0