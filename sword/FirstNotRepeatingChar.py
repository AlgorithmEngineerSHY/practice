from collections import Counter
class Solution:
    def FirstNotRepeatingChar(self, s):
        counter = Counter(s)
        n_one_list = [x for x in counter if counter[x] == 1]
        if not n_one_list:
            return -1
        res = len(s)
        for i in n_one_list:
            tmp_res = s.index(i)
            if tmp_res < res:
                res = tmp_res
        return res