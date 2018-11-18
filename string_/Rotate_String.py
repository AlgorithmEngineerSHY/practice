class Solution:
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A * 2




# from collections import Counter
# class Solution:
#     def rotateString(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: bool
#         """
#         if A == B:
#             return True
#         len_a = len(A)
#         len_b = len(B)
#         if len_a != len_b:
#             return False
#         c_a = Counter(A)
#         c_b = Counter(B)
#         if c_a != c_b:
#             return False
#         for i in range(len_a):
#             new_a = A[i:] + A[:i]
#             if new_a == B:
#                 return True
#         return False