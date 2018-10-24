class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        re = [True]
        wordDict = set(wordDict)
        for i in range(1, len(s) + 1):
            re.append(any([re[j] and s[j:i] in wordDict for j in range(i)]))
        return re[-1]