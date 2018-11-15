class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return []
        len_nums = len(nums)
        if len_nums == 1:
            return [str(nums[0])]

        res = []
        low = high = 0
        for idx in range(1, len_nums):
            if nums[idx] - nums[idx - 1] == 1:
                high += 1
            else:
                if high - low == 0:
                    res.append(str(nums[low]))
                else:
                    res.append(str(nums[low]) + '->' + str(nums[high]))
                low = high = idx
        if low == high:
            res.append(str(nums[-1]))
        else:
            res.append(str(nums[low]) + '->' + str(nums[high]))
        return res

obj = Solution()
print(obj.summaryRanges([0,2,3,4,6,8,9]))