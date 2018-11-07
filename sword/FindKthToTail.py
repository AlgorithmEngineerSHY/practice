class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import deque
class Solution:
    def FindKthToTail(self, head, k):
        q = deque()
        if k <= 0:
            return None
        if not head:
            return None

        while head:
            if len(q) < k:
                q.append(head)
            else:
                q.popleft()
                q.append(head)
            head = head.next
        if len(q) < k:
            return None
        return q[0]