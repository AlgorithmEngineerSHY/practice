# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.re_list = []
        self.sum_ = None

    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum_: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.sum_ = sum_
        self.helper(root, 0, [])
        return self.re_list

    def helper(self, node, sum_, tmp_list):
        sum_ += node.val
        # tmp_list += str(node.val)
        if not node.left and not node.right:
            if sum_ == self.sum_:
                self.re_list.append(tmp_list + [node.val])
        if node.left:
            self.helper(node.left, sum_, tmp_list + [node.val])
        if node.right:
            self.helper(node.right, sum_, tmp_list + [node.val])
