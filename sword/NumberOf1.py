class Solution:
    def NumberOf1(self, n):
        return sum(map(int, list(bin(((1 << 32) - 1) & n)[2:])))