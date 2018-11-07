class Solution:
    def __init__(self):
        self.res = set()

    def Permutation(self, ss):
        ss = sorted(list(ss))
        self.helper(ss, '')
        return sorted(list(self.res))

    def helper(self, s_list, string):
        if len(s_list) == 1:
            self.res.add(string + s_list[0])
        mark = None
        for i, s in enumerate(s_list):
            if s != mark:
                self.helper(s_list[:i] + s_list[i + 1:], string + s)
                mark = s
