'''
Given a linked list, return the node where the cycle begins. 
If there is no cycle, return null. 
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        try:
            fast, slow = head.next, head
            while fast is not slow:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        slow = slow.next
        while slow is not head:
            slow = slow.next
            head = head.next
        return head


