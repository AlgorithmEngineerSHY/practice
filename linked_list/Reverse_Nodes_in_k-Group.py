'''
Given a linked list, 
reverse the nodes of a linked list k at a time and return its modified list.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 1:
            return head
        first = ListNode(0)
        p = first
        num = 0
        left = head

        while head:
            num += 1
            right = head
            head = head.next

            if num == k:
                num = 0
                right.next = None
                left_node, right_node = self.reverse_node(left, right)
                p.next = left_node
                p = right_node
                left = head
        p.next = left
        return first.next


    def reverse_node(self, left, right):
        last = None
        re_last = left
        while left:
            left_next = left.next
            left.next = last
            last = left
            left = left_next
        return right, re_last

