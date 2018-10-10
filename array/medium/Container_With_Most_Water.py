'''
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        re = 0
        head, tail = 0, len(height) - 1
        for i in range(len(height)):
            width = abs(head - tail)
            if height[head] < height[tail]:
                tmp_re = width * height[head]
                head += 1
            else:
                tmp_re = width * height[tail]
                tail -= 1
            if tmp_re > re:
                re = tmp_re
        return re
