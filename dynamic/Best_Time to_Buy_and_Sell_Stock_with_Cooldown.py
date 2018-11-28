class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        len_prices = len(prices)
        s_0 = [0] * len_prices
        s_1 = [0] * len_prices
        s_2 = [0] * len_prices
        s_1[0] = -prices[0]
        s_2[0] = -float('inf')
        for i in range(1, len_prices):
            s_2[i] = s_1[i - 1] + prices[i]
            s_0[i] = max(s_2[i - 1], s_0[i - 1])
            s_1[i] = max(s_0[i - 1] - prices[i], s_1[i - 1])
        return max(s_0[-1], s_2[-1])


