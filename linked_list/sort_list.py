'''
Sort a linked list in O(n log n) time using constant space complexity.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        re = self.merge(left, right)
        return re

    def merge(self, left, right):
        first = ListNode(0)
        p = first
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        if left:
            p.next = left
        if right:
            p.next = right
        return first.next



