
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        res = [1]
        idx_2, idx_3, idx_5 = 0, 0, 0
        for i in range(index - 1):
            helper = [res[idx_2] * 2, res[idx_3] * 3, res[idx_5] * 5]
            min_num = min(helper)
            res.append(min_num)
            if helper[0] == min_num:
                idx_2 += 1
            if helper[1] == min_num:
                idx_3 += 1
            if helper[2] == min_num:
                idx_5 += 1
        return res[-1]

obj = Solution()
print(obj.GetUglyNumber_Solution(1))