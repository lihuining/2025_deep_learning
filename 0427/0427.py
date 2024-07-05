# n = int(input())
# nums = list(map(int,input.split()))
n = 5
a = [1,2,3,4,5]
pre = [0]*n
suf = [0]*n
cur = 0
for i in range(1,n,2):
    cur += a[i]*a[i-1]
    pre[i] = cur
cur = 0
for i in range(n-2,-1,-2):
    cur += a[i]*a[i+1]
    suf[i] = cur
ans = []
print(pre,suf)
for i in range(n):
    x = 0
    if i % 2 == 0:
        if i - 1 >= 0:
            x += pre[i-1]
        if i + 1 < n:
            x += suf[i+1]
    else:
        if i - 2 >= 0:
            x += pre[i-2]
        if i + 2 < n:
            x += suf[i+2]
        x += a[i-1]*a[i+1]
    print(x)