class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        first = ListNode(0)
        first.next = pHead

        fast, slow = first, first

        while fast == first or fast != slow:
            if slow.next:
                slow = slow.next
            else:
                return None
            if fast.next.next:
                fast = fast.next.next
            else:
                return None
        helper = first
        while helper != slow:
            helper = helper.next
            slow = slow.next
        return slow

a=ListNode(0)
a.next=ListNode(1)
a.next.next=ListNode(2)
a.next.next.next=ListNode(3)
a.next.next.next.next=a.next
obj=Solution()
print(obj.EntryNodeOfLoop(a).val)





