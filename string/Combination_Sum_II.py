class Solution:
    def __init__(self):
        self.candidates = None
        self.res = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.candidates = candidates
        self.dfs(0, [], target)
        return self.res

    def dfs(self, idx, path, tmp_target):
        if tmp_target == 0:
            self.res.append(path)
            return None
        if tmp_target < 0:
            return None
        for i in range(idx, len(self.candidates)):
            if i > idx and self.candidates[i] == self.candidates[i - 1]:
                continue
            self.dfs(i + 1, path + [self.candidates[i]], tmp_target - self.candidates[i])

obj = Solution()
print(obj.combinationSum2([10,1,2,7,6,1,5], 8))