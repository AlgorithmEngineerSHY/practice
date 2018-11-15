# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        first = ListNode(0)
        first.next = head
        odd = head
        if head.next:
            even = head.next
        else:
            return head
        first_even = head.next
        while even:
            if even.next:
                new_odd = even.next
                new_even = new_odd.next
                odd.next = new_odd
                odd = new_odd
                odd.next = first_even
                even.next = new_even
                even = new_even
            else:
                break
        return first.next
