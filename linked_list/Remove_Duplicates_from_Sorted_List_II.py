'''
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        list_1 = []
        dup_set = set()
        dup_num = None
        while head:
            # print('wsnd')
            list_1.append(head.val)
            if dup_num != head.val:
                dup_num = head.val
            else:
                dup_set.add(dup_num)
            head = head.next
        first = ListNode(0)
        p = first
        # print(dup_set)
        for i in list_1:
            if i not in dup_set:
                # print('nmsl')
                p.next = ListNode(i)
                p = p.next
        return first.next
a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(2)
b=Solution()
b.deleteDuplicates(a)



