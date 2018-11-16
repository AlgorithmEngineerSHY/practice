from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for i in '!?\',;.':
            paragraph = paragraph.replace(i, ' ')

        paragraph = paragraph.split(' ')

        paragraph = [x.lower() for x in paragraph if x.isalpha()]
        c = Counter(paragraph)
        for i in banned:
            if i in c:
                c[i] = 0
        max_freq = max(c.values())
        for i in c:
            if c[i] == max_freq:
                return i

obj = Solution()
print(obj.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))