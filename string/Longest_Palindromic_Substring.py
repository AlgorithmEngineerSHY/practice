class Solution:
    def __init__(self):
        self.s = None
        self.len_s = None
        self.max_len = 0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''


        start = end = 0
        self.s = s
        self.len_s = len(s)

        for i in range(self.len_s):

            len_1 = self.helper(i, i)
            len_2 = self.helper(i, i + 1)
            len_ = max(len_1, len_2)
            if len_ > self.max_len:
                self.max_len = len_
                start = i - (len_ - 1) // 2
                end = i + len_ // 2
        return s[start: end + 1]


    def helper(self, left, right):
        while left >= 0 and right < self.len_s:
            if self.s[left] == self.s[right]:
                left -= 1
                right += 1
            else:
                break
        return right - left - 1