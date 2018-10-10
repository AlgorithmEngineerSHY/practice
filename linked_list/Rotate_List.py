'''
Given a linked list, rotate the list to the right by k places, 
where k is non-negative.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        num = 1
        last = head
        while last.next:
            num += 1
            last = last.next
        k = k % num
        if k == 0:
            return head
        cut = num - k
        p = head
        for i in range(cut - 1):
            p = p.next
        first = p.next
        p.next = None
        last.next = head
        return first

