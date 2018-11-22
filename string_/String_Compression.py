
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        idx = 0
        c = chars[0]
        n_c = 1
        for i, char in enumerate(chars[1:]):
            if char == c:
                n_c += 1
            else:
                if n_c == 1:
                    chars[idx] = c
                    idx += 1
                else:
                    chars[idx] = c
                    idx += 1
                    for j in str(n_c):
                        chars[idx] = j
                        idx += 1
                    n_c = 1
                c = chars[i + 1]
        if n_c == 1:
            chars[idx] = c
            idx += 1
        else:
            chars[idx] = c
            idx += 1
            for j in str(n_c):
                chars[idx] = j
                idx += 1
        return idx


obj = Solution()
print(obj.compress(["a"]))