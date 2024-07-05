mod = 10**9 + 7
n = int(input())
num = n*(n-1)*(n-2) // 6
print(num*pow(26,n-1,mod)%mod)