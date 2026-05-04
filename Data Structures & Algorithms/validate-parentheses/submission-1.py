class Stack:
    def __init__():
        self.array = []

    def pop(self):
        if len(self.array == 0):
            return False
        self.array.pop() 

class Solution:
    def isValid(self, s: str) -> bool:
        # loop over s
        # push open brackets onto stack
        # when encoutering a close bracket: pop from stack
        # bracket types must match
        # continue until stack is empty
        # return true
        
        stack = []
        for symbol in s:
            if symbol == ")":
                if len(stack) == 0:
                    return False
                prev_symbol = stack.pop()
                isValid = (prev_symbol == "(")
                if not isValid:
                    return False

            elif symbol == "]":
                if len(stack) == 0:
                    return False
                prev_symbol = stack.pop()
                isValid = (prev_symbol == "[")
                if not isValid:
                    return False

            elif symbol == "}":
                if len(stack) == 0:
                    return False
                prev_symbol = stack.pop()
                isValid = (prev_symbol == "{")
                if not isValid:
                    return False

            else:
                stack.append(symbol)

        if len(stack) != 0:
            return False

        return True 
        