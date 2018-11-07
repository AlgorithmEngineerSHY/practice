class Solution:

    def IsPopOrder(self, pushV, popV):
        stack = []
        idx_push = 0
        idx_pop = 0
        len_push = len(pushV)
        for i in popV:
            if not stack:
                stack.append(pushV[idx_push])
                idx_push += 1
            while stack[-1] != i:
                if idx_push < len_push:
                    stack.append(pushV[idx_push])
                    idx_push += 1
                else:
                    break
            if stack[-1] == i:
                stack.pop()
                idx_pop += 1
            else:
                break
        return len_push == idx_pop
obj = Solution()
print(obj.IsPopOrder([1,2,3,4,5], [4,5,3,2,1]))