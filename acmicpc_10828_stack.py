
import sys
stack = []


def push(val):
    stack.append(val)


def pop():
    if not stack:
        return '-1'
    return stack.pop()


def size():
    return len(stack)


def empty():
    return 0 if stack else 1


def top():
    return stack[-1] if stack else -1

t = int(sys.stdin.readline())
for _ in range(t):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        print(pop())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "top":
        print(top())


'''
import sys

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self,top):
        self.top = None

    def push(self, val):
        self.top = Node(int(val), self.top)

    def pop(self):
        if not self.top:
            return '-1'
        node = self.top
        self.top = node.next
        return node.item

    def size(self):
        return len(stack)

    def empty(self):
        return not stack

    def top(self):
        return self.top


t = int(sys.stdin.readline())
for i in range(t):
    cmd = sys.stdin.readline().split()
    print(cmd)
    print(cmd[1])
    if cmd[0] == 'push':
        T.push(cmd[1])
    elif cmd[0] == 'pop':
        T.pop()
    elif cmd[0] == 'size':
        T.size()
    elif cmd[0] == 'empty':
        T.empty()
    elif cmd[0] == 'top':
        T.top()
'''