class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            else:
                if len(stack) == 0:
                    return False
                else:
                    check = stack.pop()
                    if i == check:
                        continue
                    else:
                        return False
        if len(stack) != 0:
            return False
        return True