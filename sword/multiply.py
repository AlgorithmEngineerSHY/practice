
class Solution:
    def multiply(self, A):
        # write code here
        len_A = len(A)
        if not len_A:
            return []
        if len_A == 1:
            return [1]
        if len_A == 2:
            return [A[1], A[0]]

        B1 = [1] * len_A
        B1[1] = A[0]
        for i in range(2, len_A):
            B1[i] *= B1[i - 1] * A[i - 1]

        B2 = [1] * len_A
        B2[-2] = A[-1]
        for i in range(2, len_A):
            B2[len_A - i - 1] *= B2[len_A - i] * A[len_A - i]
        B = zip(B1, B2)
        B = [x[0] * x[1] for x in B]
        return B
obj = Solution()
print(obj.multiply([1,2,3]))