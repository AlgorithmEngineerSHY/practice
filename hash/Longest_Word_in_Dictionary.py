from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.is_end = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for w in word:
            p = p.child[w]
        p.is_end = True
        p.word = word

    def has_word(self, word):
        p = self.root
        for w in word:
            p = p.child.get(w)
            if p is None:
                return False
        if p.is_end:
            return True
        else:
            return False

    def has_prefix(self, prefix):
        p = self.root
        for i in prefix:
            p = p.child.get(i)
            if p is None:
                return False
        return True

    def bfs(self, word):
        p = self.root
        for w in word:
            p = p.child.get(w)
            if p is None:
                return False
            if not p.is_end:
                return False
        if p.is_end:
            return True
        else:
            return False

class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = ''
        for word in words:
            if len(word) > len(res) or len(word) == len(res) and word < res:
                if trie.bfs(word):
                    res = word
        return res