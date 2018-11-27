class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        len_num = len(num)
        if len_num == k:
            return '0'
        if k == 0:
            return num
        drop_set = set()
        stack = [0]
        for i in range(1, len_num):
            if num[i] >= num[stack[-1]]:
                stack.append(i)
            else:
                while stack and num[stack[-1]] > num[i] and k > 0:
                    drop_set.add(stack.pop())
                    k -= 1
                stack.append(i)
            if k == 0:
                break
        while k:
            drop_set.add(stack.pop())
            k -= 1
        res = [x for i, x in enumerate(num) if i not in drop_set]
        res = ''.join(res).lstrip('0')
        if not res:
            return '0'
        else:
            return res

obj = Solution()
print(obj.removeKdigits("112", 1))

