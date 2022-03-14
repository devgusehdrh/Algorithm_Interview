import sys
input = sys.stdin.readline

stack = []
result = []
count = 1

t = int(input())

for i in range(t):
    num = int(input())
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1

    if len(stack) and num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        break

if not stack:
    print('\n'.join(result))
