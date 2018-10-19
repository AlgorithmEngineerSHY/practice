class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_idx = len(nums) - 1
        start, end, step = 0, 0, 0
        while end < last_idx:
            max_idx = end
            step += 1
            for idx in range(start, end + 1):
                tmp = nums[idx] + idx
                if tmp >= last_idx:
                    return step
                max_idx = max(max_idx, tmp)
            start, end = end + 1, max_idx
        return step