class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evens = list(filter(lambda x: x % 2 == 0, A))
        odds = list(filter(lambda x: x % 2 != 0, A))
        return [evens.pop() if x % 2 == 0 else odds.pop() for x in range(len(A))]
