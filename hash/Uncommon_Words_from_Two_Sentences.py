from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split(' ')
        B = B.split(' ')
        c_a = Counter(A)
        c_b = Counter(B)
        a = set([x for x in c_a if c_a[x] == 1])
        b = set([x for x in c_b if c_b[x] == 1])
        return list(a.union(b).difference(set(A).intersection(set(B))))

obj = Solution()
print(obj.uncommonFromSentences("s z z z s", "s z ejt"))