class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(i)
            else:
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(int(eval(f'({b}){i}({a})')))
        return int(stack[0])


a = Solution()
print(a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
