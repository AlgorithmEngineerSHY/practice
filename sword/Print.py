class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = [[pRoot.val]]
        stack = [pRoot]
        while stack:
            tmp_stack = []
            tmp_res = []
            for i in range(len(stack)):
                if stack[i].left:
                    tmp_stack.append(stack[i].left)
                    tmp_res.append(stack[i].left.val)
                if stack[i].right:
                    tmp_stack.append(stack[i].right)
                    tmp_res.append(stack[i].right.val)
            if tmp_res:
                res.append(tmp_res)
            stack = tmp_stack
        return res
obj = Solution()
a=TreeNode(0)
a.left=TreeNode(1)
a.right=TreeNode(2)
print(obj.Print(a))