import sys
from collections import defaultdict

site = defaultdict(str)

M, N = map(int,input().split())
for i in range(M):
    input = sys.stdin.readline().split()
    site[input[0]] =input[1]

for i in range(N):
    input = sys.stdin.readline().strip()
    print(site[input])