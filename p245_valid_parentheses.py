class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for i in s:
            if s not in table:
                stack.append(s)
            elif not stack or table[s] != stack[-1]:
                return False
            else:
                stack.pop()
        return len(stack) == 0