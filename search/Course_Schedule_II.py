
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degree = dict([(i, 0) for i in range(numCourses)])
        graph = [[] for _ in range(numCourses)]
        res = []
        for i, j in prerequisites:
            degree[j] += 1
            graph[i].append(j)
        zero_degree_stack = []
        drop = []
        for i in degree:
            if degree[i] == 0:
                zero_degree_stack.append(i)
                drop.append(i)
        for i in drop:
            degree.pop(i)

        for i in range(numCourses):
            if zero_degree_stack:
                node = zero_degree_stack.pop()
                res.append(node)
                for j in graph[node]:
                    degree[j] -= 1
                    if degree[j] == 0:
                        zero_degree_stack.append(j)
                        degree.pop(j)
            else:
                return []
        res.reverse()
        return res