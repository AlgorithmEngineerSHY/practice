class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []

        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


# class Solution:
#     def __init__(self):
#         self.nums = None
#
#     def constructMaximumBinaryTree(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """
#         self.nums = nums
#         return self.helper(0, len(nums) - 1)
#
#     def helper(self, i, j):
#         if i > j:
#             return None
#         max_val = max(self.nums[i: j + 1])
#         max_idx = self.nums.index(max_val)
#         node = TreeNode(max_val)
#         node.left = self.helper(i, max_idx - 1)
#         node.right = self.helper(max_idx + 1, j)
#         return node


