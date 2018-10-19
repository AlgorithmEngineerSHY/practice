from collections import Counter
class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not s or not t:
            return ''
        t_counter = Counter(t)
        t_set = set(t)
        len_t = len(t_set)
        s_counter = Counter()
        last_idx_s = len(s) - 1
        left, right = 0, 0
        re_dict = {'left': None, 'right': None, 'min_len': last_idx_s + 1}
        tmp = 0
        while right <= last_idx_s:
            s_right = s[right]
            if s_right in t_set:
                s_counter[s_right] += 1

                if t_counter[s_right] == s_counter[s_right]:
                    tmp += 1
                while tmp == len_t:
                    if right - left + 1 <= re_dict['min_len']:
                        re_dict['left'] = left
                        re_dict['right'] = right
                        re_dict['min_len'] = right - left + 1
                    s_left = s[left]
                    if s_left in t_set:
                        s_counter[s_left] -= 1
                        if t_counter[s_left] > s_counter[s_left]:
                            tmp -= 1
                    left += 1
            right += 1

        if re_dict['left'] is not None:
            return s[re_dict['left']: re_dict['right'] + 1]
        else:
            return ''
obj=Solution()
print(obj.minWindow("ADOBECODEBANC","ABC"))