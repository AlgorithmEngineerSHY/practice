class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        len_s = len(s)
        if len_s < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len_s
        return max(self.longestSubstring(x, k) for x in s.split(c))