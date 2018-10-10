'''
Given a linked list, 
remove the n-th node from the end of list and return its head.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        first = ListNode(0)
        first.next = head
        left = right = first
        for i in range(n):
            right = right.next
        while right and right.next:
            left = left.next
            right = right.next
        tmp = left.next.next
        left.next = tmp
        return first.next









