T = int(input())
from collections import defaultdict
for _ in range(T):
    N,M = map(int, input().split())
    C = list(map(int, input().split()))
    graph = defaultdict(lambda: [])
    for _ in range(M):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    DP = [[-1]*(N+1) for _ in range(N+1)]
    DP[1][N] = 0
    for i in range(N):
        for j in range(N):
            if DP[i][N-j] != -1:
                for k in graph[i]:
                    for l in graph[N-j]:
                        if C[k-1] != C[l-1]:
                            if DP[k][l] != -1:
                                DP[k][l] = min(DP[i][N-j]+1,DP[k][l])
                            else:
                                DP[k][l] = DP[i][N-j]+1
    print(DP)
    print(graph)
    print(DP[N][1])



