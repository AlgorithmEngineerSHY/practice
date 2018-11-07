class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        first = ListNode(0)
        tmp = first
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                tmp.next = pHead1
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                pHead2 = pHead2.next
            tmp = tmp.next
        if pHead1:
            tmp.next = pHead1
        if pHead2:
            tmp.next = pHead2
        return first.next
