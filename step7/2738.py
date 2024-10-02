n,m = map(int, input().split())

ma = []
for _ in range(n):
    ma.append(list(map(int, input().split())))

mb = []
for _ in range(n):
    mb.append(list(map(int, input().split())))

for i in range(n):
    result = []
    for j in range(m):
        result.append(ma[i][j] + mb[i][j])
    print(' '.join(map(str, result)))
