import math

class Solution:
    def paint_tree_of_string(self, n_leaves):
        '''

        :param n_leaves: num of leaves.
        :return: String
        '''

        len_tree = math.log2(n_leaves)
        res = ['x'*n_leaves]
        for i in range(int(len_tree)):
            mark = left = right = 0
            helper = set()
            for j, k in enumerate(res[-1]):
                if k == 'x':
                    mark += 1
                    if mark == 1:
                        left = j
                    if mark == 2:
                        mark = 0
                        right = j
                        mid = round((left + right + 1) / 2)
                        helper.add(mid)
            tmp_re = ['-x'[i in helper] for i in range(n_leaves)]
            tmp_re = ''.join(tmp_re)
            res.append(tmp_re)
        res = '\n'.join(reversed(res))
        return res

obj = Solution()
print(obj.paint_tree_of_string(16))