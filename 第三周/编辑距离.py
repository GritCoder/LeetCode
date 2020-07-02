# 动态规划
def solution(word1, word2):
    n, m = len(word1), len(word2)
    # 有一个为空串
    if n * m == 0:
        return n+m
    # 构建dp数组
    dp = [[0]*(m+1) for _ in range(n+1)]
    # print(dp)
    # 边界初始化
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j
    # 正式循环
    # 只要是从前往后的递推,一般都是下标从1开始的
    for i in range(1, n+1):
        for j in range(1, m+1):
            left = dp[i][j-1] + 1
            up = dp[i-1][j] + 1
            left_up = dp[i-1][j-1] + 1 if word1[i-1] != word2[j-1] else dp[i-1][j-1]
            dp[i][j] = min(left, up, left_up)
    return dp[n][m]
print(solution("horse", "ros"))