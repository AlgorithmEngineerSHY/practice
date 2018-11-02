class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import Counter
class Solution:
    def deleteDuplication(self, pHead):
        val_list = []
        while pHead:
            val_list.append(pHead.val)
            pHead = pHead.next
        val_counter = Counter(val_list)
        val_list = [x for x in val_counter if val_counter[x] == 1]
        val_list.sort()
        first = ListNode(0)
        p = first
        for i in val_list:
            p.next = ListNode(i)
            p = p.next
        p.next = None
        return first.next
