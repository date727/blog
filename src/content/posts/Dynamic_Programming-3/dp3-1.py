import sys
input = lambda:sys.stdin.readline().strip()
N,V = map(int,input().split())
dp = [0] * (V+1)
for i in range(1,N+1):
    v,w,s= map(int,input().split())
    if v*s >= V:
        #完全背包
        for j in range(v,V+1):
            dp[j] = max(dp[j],dp[j-v]+w)
    else:
        #0-1背包
        for j in range(V,v-1,-1):
            for k in range(0,s+1):
                if j >= k*v:
                    dp[j] = max(dp[j],dp[j-k*v]+k*w)
print(dp[V])
