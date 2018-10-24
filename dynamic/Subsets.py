class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        re = [[]]
        for num in nums:
            tmp_re = []
            for set_ in re:

                tmp_re.append(set_ + [num])
            re = re + tmp_re
        return re
obj = Solution()
print(obj.subsets([2,2]))