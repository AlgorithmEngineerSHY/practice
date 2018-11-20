class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.median(nums, k)

    def part(self, nums, start, end):
        mid = nums[end]
        left = start
        right = end
        while left < right:
            while left < right and nums[left] <= mid:
                left += 1
            while left < right and nums[right] >= mid:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[end] = nums[end], nums[left]
        return left

    def median(self, nums, k):
        len_nums = len(nums)
        k = len_nums - k
        left = 0
        right = len_nums - 1
        self.shuffle(nums)
        tmp_idx = self.part(nums, left, right)
        while True:
            if k == tmp_idx:
                return nums[k]
            elif tmp_idx < k:
                left = tmp_idx + 1
                tmp_idx = self.part(nums, left, right)
            else:
                right = tmp_idx - 1
                tmp_idx = self.part(nums, left, right)
    def shuffle(self, nums):
        from random import randint
        len_nums = len(nums)
        for i in range(len_nums):
            rand_num = randint(0, len_nums - 1)
            nums[i], nums[rand_num] = nums[rand_num], nums[i]

obj = Solution()
obj.findKthLargest([1], 1)