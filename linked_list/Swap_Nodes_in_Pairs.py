'''
Given a linked list, 
swap every two adjacent nodes and return its head.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        first = ListNode(0)
        p = first

        while head and head.next:
            tmp = head.next.next

            p.next = head.next
            p.next.next = head
            p = p.next.next
            head = tmp
        p.next = head
        return first.next

