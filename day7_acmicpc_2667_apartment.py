n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

rows = len(graph[0])
cols = len(graph)
result = []
cnt = 0
a_cnt = 0

def dfs(x,y):
    if x < 0 or y < 0 or x >= rows or y >= cols or graph[x][y] == 0:
        return
    global a_cnt
    a_cnt += 1
    graph[x][y] = 0

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

for i in range(len(graph[0])):
    for j in range(len(graph)):
        if graph[i][j] == 1:
            a_cnt = 0
            dfs(i,j)
            cnt += 1
            result.append(a_cnt)

print(cnt)
result.sort()
for i in range(cnt):
    print(result[i])




#
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# rows, cols = len(graph[0]),len(graph)
# result = []
# cnt = 0
#
#
# def dfs(x,y):
#     global cnt
#     if x < 0 or y < 0 or x >= rows or y >= cols or graph[x][y] == 0:
#         return
#     cnt += 1
#     graph[x][y] = 0
#
#     dfs(x+1,y)
#     dfs(x-1,y)
#     dfs(x,y+1)
#     dfs(x,y-1)
#
# for i in range(len(graph[0])):
#     for j in range(len(graph)):
#         if graph[i][j] == 1:
#             dfs(i,j)
#             result.append(cnt)
#             cnt = 0
#
# print(len(result))
# result.sort()
# for i in range(len(result)):
#     print(result[i])