from collections import deque
class Solution:

    def FindContinuousSequence(self, tsum):
        res = []
        left, right = 1, 2
        sum_ = 3
        q = deque([1, 2])

        while right <= tsum // 2 + 1:
            if sum_ == tsum:
                res.append(list(q))
                right += 1
                q.append(right)
                sum_ += right
            elif sum_ < tsum:
                right += 1
                q.append(right)
                sum_ += right
            else:
                sum_ -= left
                left += 1
                q.popleft()
        return res

obj = Solution()
print(obj.FindContinuousSequence(100))


