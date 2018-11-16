from collections import Counter
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        re_nums = list(reversed(nums))
        c = Counter(nums)
        max_degree = max(c.values())
        max_nums = [x for x in c if c[x] == max_degree]
        len_nums = len(nums)
        res = []
        for num in max_nums:
            left_idx = nums.index(num)
            right_idx = len_nums - re_nums.index(num) - 1

            res.append(right_idx - left_idx + 1)
        return min(res)
obj = Solution()
print(obj.findShortestSubArray([49999,1,1,1,2,1]))