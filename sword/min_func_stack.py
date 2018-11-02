class Solution:
    def __init__(self):
        self.stack = []
        self.min_1 = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_1 or self.min_1[-1] > node:
            self.min_1.append(node)

    def pop(self):
        if self.stack[-1] == self.min_1[-1]:
            self.stack.pop()
            self.min_1.pop()
        else:
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_1[-1]
