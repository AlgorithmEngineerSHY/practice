from collections import Counter
class Solution:
    def FindNumsAppearOnce(self, array):
        c = Counter(array)
        return [x for x in c if c[x] == 1]