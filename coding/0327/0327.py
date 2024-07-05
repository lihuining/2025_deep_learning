'''
删除一段区间让数组有序
'''
n = 3
a = [1,2,3] # 数组长度
l = 0 # [0,l] 有序
while l <= n -1 and a[l] <= a[l+1]:
    l += 1
r = n - 1  # [r,n-1] 有序
while r >= 1 and a[r] >= a[r-1]:
    r -= 1
if l >= r:
    print(n*(n+1)//2)
j = r
ans = n -j + 1 # 左边区间全部删去？
for i in range(l+1): # 遍历左边界起点，此时可以删除的范围为[i,j]...[i,n-1]
    while j < n and a[j] < a[i]:
        j += 1
    ans += n-j+1
print(ans)


