from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ct = Counter()
        for num_site in cpdomains:
            num, site = num_site.split(' ')
            num = int(num)
            ss = site.split('.')[::-1]
            tmp = ''
            for s in ss:
                tmp = s + '.' + tmp
                ct[tmp[:-1]] += num
        res = []
        for key in ct:
            res.append(str(ct[key]) + ' ' + key)
        return res

obj = Solution()
print(obj.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))