'''
Implement next permutation, 
which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, 
it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
'''


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            self.reverse(nums, 0)
            return
        j = len(nums) - 1
        while j >=0 and nums[j] <= nums[i]:
            j -= 1
        # print(i, j)
        self.swap(nums, i, j)
        self.reverse(nums, i + 1)
        # print(nums)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, i):
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
# a=[3,2,1]
# b=Solution()
# b.nextPermutation(a)