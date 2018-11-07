from collections import Counter
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        ct = Counter(numbers)
        for i in ct:
            if i != 0 and ct[i] > 1:
                return False
        numbers.sort()
        num_0 = 0
        if 0 in ct:
            num_0 = ct[0]
        numbers = [x for x in numbers if x != 0]
        diff = 0
        for i in range(1, len(numbers)):
            diff += numbers[i] - numbers[i - 1] - 1
        if diff <= num_0:
            return True
        else:
            return False

