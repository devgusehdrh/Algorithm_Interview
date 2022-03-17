import sys, collections

q = collections.deque()


def push(val):
    q.append(val)


def pop():
    return -1 if not q else q.popleft()


def size():
    return len(q)


def empty():
    return 1 if not q else 0


def front():
    return -1 if not q else q[0]


def back():
    return -1 if not q else q[-1]


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'push':
        push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(pop())
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        print(empty())
    elif cmd[0] == 'front':
        print(front())
    elif cmd[0] == 'back':
        print(back())

