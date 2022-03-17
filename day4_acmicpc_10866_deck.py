import sys
import collections

d = collections.deque()

def push_f(val):
    d.appendleft(val)
    return
def push_b(val):
    d.append(val)
    return
def pop_f():
    return -1 if not d else d.popleft()
def pop_b():
    return -1 if not d else d.pop()
def size():
    return len(d)
def empty():
    return 1 if not d else 0
def front():
    return -1 if not d else d[0]
def back():
    return -1 if not d else d[-1]

t = int(sys.stdin.readline())
for _ in range(t):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "push_front":
        push_f(cmd[1])
    elif cmd[0] == "push_back":
        push_b(cmd[1])
    elif cmd[0] == "pop_front":
        print(pop_f())
    elif cmd[0] == "pop_back":
        print(pop_b())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "front":
        print(front())
    elif cmd[0] == "back":
        print(back())