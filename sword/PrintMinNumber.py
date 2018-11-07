from functools import cmp_to_key
class Solution:
    def PrintMinNumber(self, numbers):
        str_num = list(map(str, numbers))
        str_num.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
        return ''.join(str_num)

obj = Solution()
print(obj.PrintMinNumber(['21', '2']))

