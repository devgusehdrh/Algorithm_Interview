def isstack(s):
    stack = []
    table = {')': '('}

    for i in s:
        if i not in table:
            stack.append(i)
        elif not stack or table[i] != stack.pop():
            return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


arr = []
t = int(input())
for _ in range(t):
    data = input()
    result = isstack(data)
    print(result)