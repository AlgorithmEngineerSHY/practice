
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        res = -1
        for i in rotateArray:
            if i >= res:
                res = i
            else:
                return i
        return rotateArray[0]