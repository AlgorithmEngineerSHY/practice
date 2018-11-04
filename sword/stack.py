from collections import deque
class Solution:
    def __init__(self):
        self.stack = deque()
    def push(self, node):
        self.stack.append(node)

    def pop(self):
        if self.stack:
            return self.stack.popleft()
        else:
            return None