'''
 A linked list is given such that each node contains an additional random pointer 
 which could point to any node in the list or null.
Return a deep copy of the list. 
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def __init__(self):
        self.hash_node = {}
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        if head in self.hash_node:
            return self.hash_node[head]
        new_node = RandomListNode(head.label)
        self.hash_node[head] = new_node

        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)
        return new_node



