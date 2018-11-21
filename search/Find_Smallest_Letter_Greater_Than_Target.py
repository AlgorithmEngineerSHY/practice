class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        set_let = set(letters)
        tmp = [x for x in set_let if x > target]
        if tmp:
            return min(tmp)
        else:
            return min(set_let)
