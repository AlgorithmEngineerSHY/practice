'''
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
'''


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        re = nums[0] + nums[1] + nums[2]
        lenght = len(nums) - 1
        for i in range(len(nums) - 2):
            j, k = i + 1, lenght
            while k > j:
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum == target:
                    return target
                if abs(tmp_sum - target) < abs(re - target):
                    re = tmp_sum
                if tmp_sum < target:
                    j += 1
                else:
                    k -= 1
        return re
