import sys

N = int(sys.stdin.readline().rstrip())
A = {map(int,sys.stdin.readline().rstrip().split())}
M = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
for i in nums:
    if i in A:
        print(1)
    else:
        print(0)

# A에 중복값이 없으므로 set으로 선언

