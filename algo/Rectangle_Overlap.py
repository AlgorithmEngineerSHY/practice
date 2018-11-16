class Solution:

    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        left_1 = rec1[0]
        right_1 = rec1[2]
        up_1 = rec1[3]
        down_1 = rec1[1]
        x_center_1 = (left_1 + right_1) / 2
        y_center_1 = (up_1 + down_1) / 2

        left_2 = rec2[0]
        right_2 = rec2[2]
        up_2 = rec2[3]
        down_2 = rec2[1]
        x_center_2 = (left_2 + right_2) / 2
        y_center_2 = (up_2 + down_2) / 2

        x_dis = abs(x_center_1 - x_center_2)
        y_dis = abs(y_center_1 - y_center_2)

        if x_dis < (right_1 - left_1) / 2 + (right_2 - left_2) / 2 and \
            y_dis < (up_1 - down_1) / 2 + (up_2 - down_2) / 2:
            return True
        else:
            return False




