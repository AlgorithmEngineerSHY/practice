class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        len_nums = len(nums)
        if len_nums == 1:
            return nums
        num_1 = nums[0]
        num_2 = num_1
        for i in range(1, len_nums):
            if num_1 != nums[i]:
                num_2 = nums[i]
                break
        if num_1 == num_2:
            return [num_1]
        else:
            count_1 = 0
            count_2 = 0
            for n in nums:
                if n == num_1:
                    count_1 += 1
                elif n == num_2:
                    count_2 += 1
                elif count_1 == 0:
                    count_1 = 1
                    num_1 = n
                elif count_2 == 0:
                    count_2 = 1
                    num_2 = n
                else:
                    count_1 -= 1
                    count_2 -= 1
        n_num_1 = self.count(num_1, nums)
        n_num_2 = self.count(num_2, nums)
        res = []
        if n_num_1 > len_nums // 3:
            res.append(num_1)
        if n_num_2 > len_nums // 3:
            res.append(num_2)
        return res


    def count(self, num, nums):
        res = 0
        for n in nums:
            if n == num:
                res += 1
        return res