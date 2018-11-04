class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        self.data.append(num)
        self.data.sort()


    def GetMedian(self):
        len_data = len(self.data)
        if len_data % 2 == 0:
            return (self.data[len_data // 2 - 1] + self.data[len_data // 2]) / 2


        else:
            return self.data[len_data // 2]