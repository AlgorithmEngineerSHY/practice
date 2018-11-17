class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = a.split('+')
        b = b.split('+')
        a_real = int(a[0])
        a_image = int(a[1][: -1])
        b_real = int(b[0])
        b_image = int(b[1][: -1])
        c_real = a_real * b_real - a_image * b_image
        c_image = a_real * b_image + a_image * b_real
        c = str(c_real) + '+' + str(c_image) + 'i'
        return c


obj = Solution()
print(obj.complexNumberMultiply("1+-1i", "0+0i"))
