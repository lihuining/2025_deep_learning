# n,m = list(map(int,input().split())) # n行m列
# a = [input() for _ in range(n)]
n = 3
m = 3
a = ['101', '110', '101']
b = [[0]*(m+1) for _ in range(n)] # i行j列位置右边1的数量

for i in range(n):
    for j in range(m)[::-1]:
        if a[i][j] == '1':
            b[i][j] = b[i][j+1] + 1
ans = 0
print(a,b)
for j in range(m):
    c = []
    for i in range(n):
        c.append(b[i][j])
    c.sort(reverse = True)
    print(j,c)
    for i in range(n):
        ans = max(ans,(i+1)*c[i])
print(ans)