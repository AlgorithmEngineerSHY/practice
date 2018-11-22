class Solution:
    def __init__(self):
        self.visit = None
        self.graph = None
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = [[] for _ in range(numCourses)]
        self.visit = [0 for _ in range(numCourses)]
        for i, j in prerequisites:
            self.graph[i].append(j)
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, i):
        if self.visit[i] == -1:
            return False
        if self.visit[i] == 1:
            return True
        self.visit[i] = -1
        for j in self.graph[i]:
            if not self.dfs(j):
                return False
        self.visit[i] = 1
        return True