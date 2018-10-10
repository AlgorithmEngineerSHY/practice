'''
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        first = ListNode(0)
        p = first
        q = PriorityQueue()
        num = 0
        for node in lists:
            if node:
                q.put((node.val, num, node))
                num += 1
        while q.qsize() > 0:
            p.next = q.get()[2]
            p = p.next
            if p.next:
                q.put((p.next.val, num, p.next))
                num += 1
        return first.next


    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     ListNode_1 = lists.pop()
    #     while lists:
    #         ListNode_2 = lists.pop()
    #         ListNode_1 = self.merge_node(ListNode_1, ListNode_2)
    #     return ListNode_1
    # def merge_node(self, node_1, node_2):
    #     re = ListNode(0)
    #     p = re
    #     while node_1 and node_2:
    #         if node_1.val < node_2.val:
    #             p.next = node_1
    #             node_1 = node_1.next
    #         else:
    #             p.next = node_2
    #             node_2 = node_2.next
    #         p = p.next
    #     if node_1:
    #         p.next = node_1
    #     if node_2:
    #         p.next = node_2
    #     return re.next
