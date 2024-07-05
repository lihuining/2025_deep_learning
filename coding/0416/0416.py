n,x = list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()
while i < n and x >= a[i]:
    x += a[i] // 5
    i += 1
x*=2 # 使用药剂
while i < n and x >= a[i]:
    x += a[i] // 5
    i += 1
print(x)