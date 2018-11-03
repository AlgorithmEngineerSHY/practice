class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.serialize = ''
        self.s = None
        self.len_s = None
        self.idx = 0


    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        self.s = s.split(',')
        self.len_s = len(self.s)
        return self.helper()


    def helper(self):
        if self.s[self.idx] != '#':

            node = TreeNode(int(self.s[self.idx]))
            if self.idx + 1 < self.len_s:
                self.idx += 1
                node.left = self.helper()
            if self.idx + 1 < self.len_s:
                self.idx += 1
                node.right = self.helper()
        else:
            return None

        return node