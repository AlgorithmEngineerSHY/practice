class Solution:
    def __init__(self):
        self.candidates = None
        self.res = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = candidates
        self.candidates.sort()
        self.dfs(0, [], target)
        return self.res


    def dfs(self, idx, path, tmp_target):
        if tmp_target == 0:
            self.res.append(path)
            return None
        if tmp_target < 0:
            return None
        for i in range(idx, len(self.candidates)):
            self.dfs(i, path + [self.candidates[i]], tmp_target - self.candidates[i])

obj = Solution()
print(obj.combinationSum([2,3,5], 8))
