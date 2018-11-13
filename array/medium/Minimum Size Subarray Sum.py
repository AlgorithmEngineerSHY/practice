class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
        res = float('inf')
        left = right = 0
        tmp_sum = nums[0]
        while True:
            if tmp_sum <= s:
                if tmp_sum == s:
                    res = min(res, right - left + 1)
                right += 1
                if right < len(nums):
                    tmp_sum += nums[right]
                else:
                    break
            else:
                res = min(res, right - left + 1)
                left += 1
                if left <= right:
                    tmp_sum -= nums[left - 1]
                else:
                    break
        return res

obj = Solution()
print(obj.minSubArrayLen(7, [7,3,1,2,4,3]))