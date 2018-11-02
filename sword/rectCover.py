class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        first, second = 1, 2
        for i in range(2, number):
            first, second = second, first + second
        return second