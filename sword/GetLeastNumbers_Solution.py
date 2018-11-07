class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput:
            return []
        if k > len(tinput):
            return []
        tinput.sort()
        return tinput[: k]