class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = []
        for email in emails:
            email = email.split('@')
            email[0] = email[0].replace('.', '')
            email[0] = email[0].split('+')[0]
            res.append('@'.join(email))
        return len(set(res))

obj = Solution()
print(obj.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

