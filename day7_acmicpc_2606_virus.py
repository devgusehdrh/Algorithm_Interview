n = int(input())
m = int(input())

com = [[]*n for _ in range(n+1)]
visited = set()

for i in range(m):
    f, b = map(int,input().split())
    com[f].append(b)
    com[b].append(f)

def dfs(start):
    for i in com[start]:
        if i not in visited:
            visited.add(i)
            dfs(i)
dfs(1)
print(len(visited)-1)