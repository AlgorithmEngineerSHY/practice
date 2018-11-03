from collections import Counter
class Solution:
    def GetNumberOfK(self, data, k):
        return Counter(data)[k]