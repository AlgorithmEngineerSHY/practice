class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for i in strs:
            j = ''.join(sorted(i))
            if j in result:
                result[j].append(i)
            else:
                result[j] = [i]
        result = [result[x] for x in result]
        return result
obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat", '', '']))