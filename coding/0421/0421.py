MOD = 10**9 + 7
n = int(input())
num = n*(n-1) // 2 - (n-1) # 选取不相邻的对数
print(num*25*pow(26,n-2,mod)%mod)