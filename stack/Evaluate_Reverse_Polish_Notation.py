'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. 
Each operand may be an integer or another expression.
'''


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None
        stack_1 = []
        stack_2 = []
        one_or_two = 1
        op_set = set(('+', '-', '*', '/'))
        for op in tokens:
            # print(op)
            if one_or_two == 1:
                one_or_two = 2
                if op not in op_set:
                    stack_1.append(int(op))
                else:
                    num_1 = stack_1.pop()
                    num_2 = stack_2.pop()
                    if op == '+':
                        stack_1.append(num_1 + num_2)
                    elif op == '-':
                        stack_1.append(num_1 - num_2)
                    elif op == '*':
                        stack_1.append(num_1 * num_2)
                    else:
                        stack_1.append(int(num_1 / num_2))

            else:
                one_or_two = 1
                if op not in op_set:
                    stack_2.append(int(op))
                else:
                    num_1 = stack_1.pop()
                    num_2 = stack_2.pop()
                    if op == '+':
                        stack_2.append(num_2 + num_1)
                    elif op == '-':
                        stack_2.append(num_2 - num_1)
                    elif op == '*':
                        stack_2.append(num_2 * num_1)
                    else:
                        stack_2.append(int(num_2 / num_1))
            # print(stack_1)
            # print(stack_2)
            # print('##########')
        if one_or_two == 1:
            return stack_2[0]
        else:
            return stack_1[0]
a=Solution()
b=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(a.evalRPN(b))