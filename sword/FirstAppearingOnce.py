class Solution:
    def __init__(self):
        self.repeat_set = set()
        self.single_set = set()
        self.single_list = []
    def FirstAppearingOnce(self):
        if not self.single_set:
            return '#'
        else:
            return self.single_list[0]

    def Insert(self, char):
        if char not in self.repeat_set:
            if char not in self.single_set:
                self.single_list.append(char)
                self.single_set.add(char)
            else:
                self.single_set.remove(char)
                self.repeat_set.add(char)
                self.single_list.remove(char)

obj = Solution()
obj.Insert('g')
obj.FirstAppearingOnce()
obj.Insert('o')
obj.FirstAppearingOnce()
obj.Insert('o')
obj.FirstAppearingOnce()
obj.Insert('g')
obj.FirstAppearingOnce()
obj.Insert('l')
obj.FirstAppearingOnce()
obj.Insert('e')
obj.FirstAppearingOnce()

