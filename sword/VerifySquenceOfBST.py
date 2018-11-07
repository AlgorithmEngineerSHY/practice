class Solution:
    def __init__(self):
        self.res = True

    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        self.helper(sequence)
        return self.res

    def helper(self, val_list):
        if not self.res:
            return None
        len_val = len(val_list)
        if len_val == 1 or len_val == 0:
            return None
        root_val = val_list[-1]
        idx = 0
        while val_list[idx] < root_val and idx < len_val - 1:
            idx += 1
        if idx == len_val - 1:
            self.helper(val_list[:-1])
        else:
            for i in range(idx, len_val - 1):
                if val_list[i] < root_val:
                    self.res = False
                    return None
            self.helper(val_list[:idx])
            self.helper(val_list[idx:-1])

obj = Solution()
print(obj.VerifySquenceOfBST([3,2,4,6,1,7,5]))
