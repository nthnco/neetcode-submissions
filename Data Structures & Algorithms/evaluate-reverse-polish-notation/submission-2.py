class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ("+", "-", "*", "/"):
                val_1 = int(stack.pop())
                val_2 = int(stack.pop())
                if i == "+":
                    stack.append(val_1+val_2)
                elif i == "-":
                    stack.append(val_2-val_1)
                elif i == "*":
                    stack.append(val_1*val_2)
                elif i == "/":
                    stack.append(int(val_2/val_1))
            else:
                stack.append(int(i))
        return int(stack.pop())
