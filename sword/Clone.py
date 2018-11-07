class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        node_dict = {}
        for i, node in enumerate(self.origin_node(pHead)):
            node_dict[id(node)] = i
        nodes_2 = [RandomListNode(x.label) for x in self.origin_node(pHead)]
        for node_1, node_2 in zip(self.origin_node(pHead), nodes_2):
            if node_1.next:
                node_2.next = nodes_2[node_dict[id(node_1.next)]]
            if node_1.random:
                node_2.random = nodes_2[node_dict[id(node_1.random)]]
        return nodes_2[0] if nodes_2 else None


    def origin_node(self, node):
        while node:
            yield node
            node = node.next