m,n = map(int,input().split())

q = [i+1 for i in range(m)]
result = []
cnt = 1
while q:
    if cnt == n:
        result.append(q.pop(0))
        cnt = 1
        continue
    q.append(q.pop(0))
    cnt += 1

print('<',end='')
for i, val in enumerate(result):
    if i == len(result)-1:
        print('%d' % val, end='')
    else:
        print('%d'%val,end=', ')
print('>')