'''
Reverse a linked list from position m to n. 
Do it in one-pass.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        first = ListNode(0)
        first.next = head
        left_node = first

        for i in range(m - 1):
            left_node = left_node.next
        m_node = left_node.next
        n_node = m_node
        for i in range(n - m):
            n_node = n_node.next
        right_node = n_node.next
        # reverse

        while right_node is not n_node:
            helper_node = m_node.next
            m_node.next = right_node
            right_node = m_node
            m_node = helper_node
        left_node.next = right_node
        return first.next





