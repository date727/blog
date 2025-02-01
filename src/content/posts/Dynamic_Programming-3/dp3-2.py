import sys
input = lambda:sys.stdin.readline().strip()
N,V = map(int,input().split())
dp = [0] * (V+1)
for i in range(1,N+1):
    v,w,s = map(int,input().split())
    k=1
    v_list = []
    w_list = []
    while s>=k:
        s-=k
        v_list.append(k*v)
        w_list.append(k*w)
        k*=2
    if s > 0 :
        v_list.append(s)
        w_list.append(s)
    for j in range(V, v-1,-1):
        for k in range(0, s + 1):
            if j >= k * v:
                dp[j] = max(dp[j], dp[j - k * v] + k * w)
