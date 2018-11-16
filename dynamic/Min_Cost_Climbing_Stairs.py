class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cum_cost = [0] * len(cost)
        for idx in range(2, len(cost)):
            cum_cost[idx] = min(cum_cost[idx - 2] + cost[idx - 2], cum_cost[idx - 1] + cost[idx - 1])
        return min(cum_cost[-1] + cost[-1], cum_cost[-2] + cost[-2])

obj = Solution()
print(obj.minCostClimbingStairs([10, 15, 20]))
