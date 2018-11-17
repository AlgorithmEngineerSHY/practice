class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''

        for i, j in enumerate(nums):
            while num >= j:
                result += roman[i]
                num -= j
            if num == 0:
                return result

obj = Solution()
print(obj.intToRoman(3))