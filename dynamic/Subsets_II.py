class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        tmp = None
        for i, num in enumerate(nums):
            if i == 0 or num != nums[i - 1]:
                tmp = len(res)
            tmp_re = []
            for re in res[len(res) - tmp:]:
                tmp_re.append(re + [num])
            res = res + tmp_re
        return res
obj=Solution()
print(obj.subsetsWithDup([2,2]))