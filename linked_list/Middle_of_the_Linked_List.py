# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next:
            slow = head
            fast = head.next
        else:
            return head
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        if fast:
            return slow.next
        else:
            return slow




