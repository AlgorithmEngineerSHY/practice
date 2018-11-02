class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from collections import deque
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        q = deque()
        while listNode:
            q.appendleft(listNode.val)
            listNode = listNode.next
        return list(q)