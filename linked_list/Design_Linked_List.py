class LinkListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len_link_list = 0
        self.head = None


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.len_link_list or index < 0:
            return -1
        else:
            p = self.head
            for idx in range(index):
                p = p.next
            return p.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.len_link_list += 1
        if self.head:
            node = LinkListNode(val)
            node.next = self.head
            self.head = node
        else:
            self.head = LinkListNode(val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.len_link_list += 1
        if self.head:
            p = self.head
            while p.next:
                p = p.next
            p.next = LinkListNode(val)

        else:
            self.head = LinkListNode(val)


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.len_link_list:
            return None
        elif index == 0:
            self.addAtHead(val)
        elif index == self.len_link_list:
            self.addAtTail(val)
        else:
            self.len_link_list += 1
            p = self.head
            for idx in range(1, index):
                p = p.next
            tmp = p.next
            p.next = LinkListNode(val)
            p = p.next
            p.next = tmp

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= 0 and index < self.len_link_list:
            self.len_link_list -= 1
            if index == 0:
                self.head = self.head.next
            else:
                p = self.head
                for idx in range(1, index):
                    p = p.next
                tmp = p.next.next
                p.next = tmp

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(4)
obj.addAtHead(1)
print(obj.len_link_list)
print(obj.head.val)
obj.addAtTail(3)
print(obj.len_link_list)

obj.addAtIndex(1,2)
print(obj.len_link_list)
print('nmsl',obj.head.next.val)

obj.deleteAtIndex(1)
print(obj.len_link_list)
