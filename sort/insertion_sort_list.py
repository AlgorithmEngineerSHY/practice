# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        first = ListNode(0)
        first.next = head
        cur_node = head
        while cur_node and cur_node.next:
            if cur_node.val <= cur_node.next.val:
                cur_node = cur_node.next
                continue
            else:
                tmp_node = cur_node.next
                cur_node.next = tmp_node.next
                helper_node = first
                while tmp_node.val > helper_node.next.val:
                    helper_node = helper_node.next
                tmp_node.next = helper_node.next
                helper_node.next = tmp_node
        return first.next