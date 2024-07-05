'''
n = int(input())
adj = [[] for _ in range(n)] # 相连接的
for i in range(n-1): # 接下来n-1行
    u,v = list(map(int,input().split()))
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)
cnt = [1]*n
g = [[] for _ in range(n)] # 子树
def dfs(u,p):
    global cnt,g
    for v in adj[u]:
        if v != p:
            dfs(v,u)
            cnt[u] += cnt[v]
            g[u].append(v)
dfs(0,-1) # 当前节点，parent
ans = 0
for i in range(n): # 遍历n个节点
    b = []
    for j in g[i]:
        b.append(cnt[j])
    b.sort()
    print(b)
    if b:
        ans += b[-1] - b[0] # 权值为子树极差
print(ans)
'''
n = int(input())
a = list(map(int,input().split()))
even = odd = 0
for i in a:
    if i % 2:
        odd += 1
    else:
        even += 1
ans = (odd*odd+even*even - n) // 2
for i in range(1,n):
    if (a[i] + a[i-1]) % 2 == 0:
        ans -= 1
print(ans)

