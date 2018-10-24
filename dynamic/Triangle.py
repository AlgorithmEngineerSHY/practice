class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        helper = [triangle[0][0]]
        for lis in triangle[1:]:
            tmp_helper = [0] * len(lis)
            tmp_helper[0] = lis[0] + helper[0]
            tmp_helper[-1] = lis[-1] + helper[-1]
            for i, num in enumerate(lis[1:-1]):
                tmp_helper[i + 1] = num + min(helper[i], helper[i + 1])
            helper = tmp_helper
        return min(helper)

obj=Solution()
print(obj.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
