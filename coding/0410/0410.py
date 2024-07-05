T = int(input())
for i in range(T):
    n,x,k = list(map(int,input().split()))
    ans = [0]*(n+1)
    ans[-1] = x
    for j in range(n-1,-1,-1):
        ans[j] = ans[j+1] % j
    print(ans[k-1])
    