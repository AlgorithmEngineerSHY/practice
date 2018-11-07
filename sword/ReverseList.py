class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        last = None

        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            if tmp:
                pHead = tmp
            else:
                break
        return pHead