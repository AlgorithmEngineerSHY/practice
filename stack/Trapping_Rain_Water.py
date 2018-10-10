'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
'''

# class Solution:
#     def __init__(self):
#         self.water = 0
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         if not height:
#             return 0
#         max_h = max(height)
#         if max_h == 0:
#             return 0
#         for h in range(1, max_h + 1):
#             # print(h)
#             self.helper(height, h)
#         return self.water
#     def helper(self, array, h):
#         i = 0
#         while array[i] <= h - 1:
#             i += 1
#         # print(i)
#         j = len(array) - 1
#         while array[j] <= h - 1:
#             j -= 1
#         # print(j)
#         for k in range(i, j):
#             if array[k] < h:
#                 self.water += 1
#                 print(k)
#         # print('##########')

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_h = len(height)
        if not height or len_h <= 2:
            return 0
        stack = []
        water = 0
        i = 0
        while i < len_h:
            if not stack or height[stack[-1]] >= height[i]:
                stack.append(i)
                i += 1
            else:
                mid = stack.pop()
                if not stack:
                    continue
                else:
                    water += (min(height[stack[-1]], height[i]) - height[mid]) * (i - stack[-1] - 1)
        return water
a=[0,1,0,2,1,0,1,3,2,1,2,1]
b=Solution()
print(b.trap(a))