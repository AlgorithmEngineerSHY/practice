# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.str_tree = None
        self.idx = -1
        self.len_str = None

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        self.str_tree = []
        self.helper_1(root)
        return '.'.join(self.str_tree)

    def helper_1(self, node):
        if node:
            self.str_tree.append(str(node.val))
            self.helper_1(node.left)
            self.helper_1(node.right)
        else:
            self.str_tree.append('#')


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split('.')
        if len(data) == 1:
            return None
        self.str_tree = data
        self.len_str = len(data)
        return self.helper_2()

    def helper_2(self):
        self.idx += 1
        if self.idx < self.len_str:
            val = self.str_tree[self.idx]
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = self.helper_2()
                node.right = self.helper_2()
            return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))