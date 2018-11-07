from collections import Counter
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        ct = Counter(numbers)
        for i in ct:
            if ct[i] > 1:
                duplication[0] = i
                return True
        return False