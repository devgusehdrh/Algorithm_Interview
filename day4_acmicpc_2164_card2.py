'''
import sys

t = int(sys.stdin.readline().rstrip())
queue = []
for i in range(t):
    queue.append(i+1)

while len(queue)>1:
    queue.pop(0)
    queue.append(queue.pop(0))
print(queue)
'''

import sys
import collections

t = int(sys.stdin.readline().rstrip())
deq = collections.deque([i for i in range(1,t+1)])
while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())
print(deq.popleft())