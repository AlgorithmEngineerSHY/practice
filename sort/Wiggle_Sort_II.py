class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        median = self.median(nums)
        len_nums = len(nums)
        index_func = lambda x: (2 * x + 1) % (len_nums | 1)
        left = 0
        right = len_nums - 1
        i = 0
        while i <= right:
            if nums[index_func(i)] > median:
                nums[index_func(i)], nums[index_func(left)] = nums[index_func(left)], nums[index_func(i)]
                left += 1
                i += 1
            elif nums[index_func(i)] < median:
                nums[index_func(i)], nums[index_func(right)] = nums[index_func(right)], nums[index_func(i)]
                right -= 1
            else:
                i += 1

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

    def median(self, nums):
        len_nums = len(nums)
        mid_idx = len_nums // 2
        left = 0
        right = len_nums - 1
        self.shuffle(nums)
        tmp_idx = self.part(nums, left, right)
        while True:
            if mid_idx == tmp_idx:
                return nums[mid_idx]
            elif tmp_idx < mid_idx:
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

# class Solution:
#     def wiggleSort(self, nums):
#         nums.sort(reverse=True)
#         len_nums = len(nums)
#         n_odds = len_nums // 2
#         nums[1::2], nums[::2] = nums[:n_odds], nums[n_odds:]
obj = Solution()
# print(obj.median([1,1,2,1,2,2,1]))
print(obj.wiggleSort([1,1,2,1,2,2,1]))