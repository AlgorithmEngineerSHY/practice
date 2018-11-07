class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        node_1 = pHead1
        node_2 = pHead2
        while node_1 != node_2:
            if node_1 == None:
                node_1 = pHead2
            else:
                node_1 = node_1.next
            if node_2 == None:
                node_2 = pHead1
            else:
                node_2 = node_2.next
        return node_1
