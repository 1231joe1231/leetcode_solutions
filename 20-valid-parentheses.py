class Solution:
    def isValid(self, s: str) -> bool:
        left_brackets = ['(', '[', '{']
        right_brackets = [')', ']', '}']
        stack = []
        for c in s:
            if c in left_brackets:
                stack.append(left_brackets.index(c))
            elif c in right_brackets:
                if len(stack) == 0:
                    return False
                elif right_brackets.index(c) == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
