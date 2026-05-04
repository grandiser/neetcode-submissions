class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == "+":
                res = (stack.pop() + stack.pop())
                stack.append(res)
            elif token == "*":
                res = (stack.pop() * stack.pop())
                stack.append(res)
            elif token == "/":
                val = stack.pop()
                res = int(float(stack.pop()) / val)
                stack.append(res)
            elif token == "-":
                val = stack.pop()
                res = stack.pop() - val
                stack.append(res)

            else:
                stack.append(int(token))
        
        return stack.pop()