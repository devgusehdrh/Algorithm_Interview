import sys

stack = []
table = {
    ')':'(',
    ']':'['
}
b = 0
while True:
    inputs = sys.stdin.readline().rstrip() # 공백문자 지우기 위해 rstrip()
    if inputs == '.':
        break
    for input in inputs:
        if input == '(' or input == '[':
            stack.append(input)
        elif stack and input in table and table[input] != stack[-1]:
            b = 1
            break
        elif not stack and input in table:

            b = 1
            break
        elif stack and input in table and table[input] == stack[-1]:
            stack.pop()
    if len(stack) == 0 and b == 0:
        print('yes')
    else:
        print('no')
        b = 0

    stack = []
