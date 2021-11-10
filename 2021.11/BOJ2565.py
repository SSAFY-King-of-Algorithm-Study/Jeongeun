n = int(input())

A = []
B = []

line_dict = {}

for i in range(n):
    a, b = map(int, input().split())
    line_dict[a] = b

sort_dict = sorted(line_dict.items(), key=lambda x : x[0])

dp = [0 for _ in range(n)]

for item in sort_dict:
    A.append(item[0])
    B.append(item[1])

for i in range(n):
    for j in range(n):
        if B[i] > B[j] and dp[i] < dp[j]:
            dp[i] = dp[j]  
    dp[i] += 1


print(n - max(dp))