class Solution:
    def ReverseSentence(self, s):
        s = s.split(' ')
        s.reverse()
        return ' '.join(s)

obj = Solution()
print(obj.ReverseSentence("I am a student."))