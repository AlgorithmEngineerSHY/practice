class Solution:
    def __init__(self):
        self.helper_list = None
        self.res = ''
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return '1'
        helper_list = [1]
        for i in range(2, n + 1):
            helper_list.append(helper_list[-1] * i)
        self.helper_list = helper_list
        num_list = list(range(1, n + 1))
        num_list = list(map(str, num_list))
        self.helper(num_list, k)
        return self.res

    def helper(self, num_list, k):

        len_num = len(num_list)
        k_1 = k // self.helper_list[len_num - 2]
        k_2 = k % self.helper_list[len_num - 2]
        if k_2 == 0:
            self.res += num_list[k_1 - 1]
            num_list.remove(num_list[k_1 - 1])
            self.res += ''.join(reversed(num_list))
        else:
            k = k_2
            self.res += num_list[k_1]
            num_list.remove(num_list[k_1])
            self.helper(num_list, k)



obj = Solution()
print(obj.getPermutation(3, 3))
