import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []

        for i in s:
            counter[i] -= 1
            if i in stack:
                continue

            while stack and i < stack[-1] and counter[stack[-1]]:
                stack.pop()

            stack.append(i)
        return ''.join(stack)