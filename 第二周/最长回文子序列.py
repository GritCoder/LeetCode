# 用公共子序列的思路来解决  先取反然后求两个串的公共子序列即可
# 注意，如果是子串的题，不能这样做，因为递推式不一样，子串有截断，了解一下
# def solution(inputs):
#     n1 = len(inputs)
#     tmp = inputs[::-1]
#     n2 = len(tmp)
#     dp = [[0] * (n1+1) for _ in range(n2+1)] # m控制的行, n控制的列
#     for i in range(1, n2+1):
#         for j in range(1, n1+1):
#             if inputs[i-1] == tmp[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#     return dp[-1][-1]
# 正常动规思路解决
# dp[i][j] 表示 inputs 的第 i 个字符到第 j 个字符组成的子串中，最长的回文序列长度是多少
def solution(inputs):
    n = len(inputs)
    # i > j 为0
    dp = [[0]*n for _ in range(n)]
    # 对角线必为1
    for i in range(n):
        dp[i][i] = 1
    # print(dp)
    # 反着遍历保证正确的状态转移
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if inputs[i] == inputs[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

print(solution("cbbd"))