class Solution:
    def FindNumbersWithSum(self, array, tsum):
        left, right = 0, len(array) - 1
        while left < right:
            sum_ = array[left] + array[right]
            if sum_ == tsum:
                return array[left], array[right]
            elif sum_ > tsum:
                right -= 1
            else:
                left += 1
        return []
