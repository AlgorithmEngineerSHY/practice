from collections import OrderedDict

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False
        if len(nums) < 2:
            return False
        order_dict = OrderedDict()
        for idx in range(len(nums)):
            key = nums[idx] // max(1, t)
            for i in (key - 1, key, key + 1):
                if i in order_dict and abs(order_dict[i] - nums[idx]) <= t:
                    return True
            order_dict[key] = nums[idx]
            if idx >= k:
                order_dict.popitem(last=False)
        return False