from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        if endWord not in wordList:
            return 0
        helper = deque()
        helper.append((beginWord, 1))

        while helper:
            last = helper.popleft()
            cur_word = last[0]
            cur_len = last[1]
            if cur_word == endWord:
                return cur_len

            for i in range(len(cur_word)):
                head = cur_word[:i]
                tail = cur_word[i + 1:]
                for j in 'qwertyuiopasdfghjklzxcvbnm':
                    if j != cur_word[i]:
                        new_word = head + j + tail
                        if new_word in wordList:
                            helper.append((new_word, cur_len + 1))
                            wordList.remove(new_word)
        return 0

obj = Solution()
print(obj.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]
))