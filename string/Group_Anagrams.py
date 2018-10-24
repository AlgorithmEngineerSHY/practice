from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        null_list = []
        for string in strs:
            if not string:
                null_list.append('')
                continue
            if not result:
                result.append([Counter(string), [string], len(string)])
            else:
                mark = 0
                for i in result:
                    if len(string) == i[2] and Counter(string) == i[0]:
                        i[1].append(string)
                        mark = 1
                        break
                if mark == 0:
                    result.append([Counter(string), [string], len(string)])
        re = [x[1] for x in result]
        if null_list:
            re.append(null_list)
        return re
obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat", '', '']))