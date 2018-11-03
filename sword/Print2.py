class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = [[pRoot.val]]
        stack = [pRoot]
        l_or_r = -1
        while stack:
            tmp_res = []
            tmp_stack = []
            len_stack = len(stack)
            for i in range(len_stack):
                if l_or_r == -1:
                    if stack[len_stack - i - 1].right:
                        tmp_res.append(stack[len_stack - i - 1].right.val)
                        tmp_stack.append(stack[len_stack - i - 1].right)
                    if stack[len_stack - i - 1].left:
                        tmp_res.append(stack[len_stack - i - 1].left.val)
                        tmp_stack.append(stack[len_stack - i - 1].left)
                else:
                    if stack[len_stack - i - 1].left:
                        tmp_res.append(stack[len_stack - i - 1].left.val)
                        tmp_stack.append(stack[len_stack - i - 1].left)
                    if stack[len_stack - i - 1].right:
                        tmp_res.append(stack[len_stack - i - 1].right.val)
                        tmp_stack.append(stack[len_stack - i - 1].right)
            l_or_r *= -1
            if tmp_res:
                res.append(tmp_res)
            stack = tmp_stack
        return res