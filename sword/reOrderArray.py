
class Solution:
    def reOrderArray(self, array):
        odd = []
        eve = []
        for i in range(len(array)):
            if array[i] % 2 == 0:
                eve.append(array[i])
            else:
                odd.append(array[i])
        return odd + eve