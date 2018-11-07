class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.res = False
        self.mark = 0
        self.tmp_mark = 0

    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return False
        if not pRoot1:
            return False

        self.num_node(pRoot2)
        self.ergodic(pRoot1, pRoot2)

        return self.res


    def helper(self, node_1, node_2):
        if self.tmp_mark == 0:
            self.res = True
            return None
        if node_2:
            if node_1:
                if node_1.val == node_2.val:
                    self.tmp_mark -= 1
                    self.helper(node_1.left, node_2.left)
                    self.helper(node_1.right, node_2.right)
                else:
                    return None

            else:
                return None
    def ergodic(self, node_1, node_2):
        if not self.res:
            self.tmp_mark = self.mark
            self.helper(node_1, node_2)
            if node_1.left:
                self.tmp_mark = self.mark
                self.ergodic(node_1.left, node_2)
            if node_1.right:
                self.tmp_mark = self.mark
                self.ergodic(node_1.right, node_2)

    def num_node(self, node):
        if node:
            self.mark += 1
            self.num_node(node.left)
            self.num_node(node.right)
