class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        nodes = [pRoot]
        while nodes:
            len_nodes = len(nodes)
            for i in range((len_nodes + 1) // 2):
                if nodes[i].left:
                    if not nodes[len_nodes - i - 1].right:
                        return False
                    else:
                        if nodes[i].left.val != nodes[len_nodes - i - 1].right.val:
                            return False
                else:
                    if nodes[len_nodes - i - 1].right:
                        return False

                if nodes[i].right:
                    if not nodes[len_nodes - i - 1].left:
                        return False
                    else:
                        if nodes[i].right.val != nodes[len_nodes - i - 1].left.val:
                            return False
                else:
                    if nodes[len_nodes - i - 1].left:
                        return False
            tmp_nodes = []
            for i in nodes:
                if i.left:
                    tmp_nodes.append(i.left)
                if i.right:
                    tmp_nodes.append(i.right)
            nodes = tmp_nodes
        return True
obj = Solution()
a = TreeNode(0)
a.left=TreeNode(1)
print(obj.isSymmetrical(a))



