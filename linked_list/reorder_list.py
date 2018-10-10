'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, 
only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        a, b = self.split_listnode(head)
        b = self.reverse_listnode(b)
        head = self.merge_listnode(a, b)
        # print(head.next.val)

    def split_listnode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        # print(head.val, mid.val)
        return head, mid

    def reverse_listnode(self, head):
        last = None
        cur_node = head
        while cur_node:
            tmp_node = cur_node.next
            cur_node.next = last
            last = cur_node
            # head = cur_node
            cur_node = tmp_node
        # print(last.val)
        return last

    def merge_listnode(self, a, b):
        a_tmp = a
        # b_tmp = b
        while b:
            b_tmp = b.next
            a_tmp_next = a_tmp.next
            a_tmp.next = b
            b.next = a_tmp_next
            a_tmp = a_tmp_next
            b = b_tmp
        return a
# head=a=ListNode(1)
# a.next=ListNode(2)
# a=a.next
# a.next=ListNode(3)
# a=a.next
# a.next=ListNode(4)
# # print(head.val)
# s=Solution()
# s.reorderList(head)
