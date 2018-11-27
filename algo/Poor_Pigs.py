class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        q = minutesToTest // minutesToDie + 1
        n = 0
        while q ** n < buckets:
            n += 1
        return n