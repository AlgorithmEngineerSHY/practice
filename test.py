import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin_array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin_array
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        array = self.origin_array.copy()
        random.shuffle(array)
        return array
# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_1)
print(param_2)