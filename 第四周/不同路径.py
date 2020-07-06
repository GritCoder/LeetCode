# 不同路径
# 动态规划思路
# def solution(m, n):
#     dp = [[0]*(m) for _ in range(n)]
#     # for j in range(m+1):
#     #     dp[0][j] = 1
#     # for i in range(n+1):
#     #     dp[i][0] = 1
#     for i in range(0, n):
#         for j in range(0, m):
#             if i == 0 or j == 0:
#                 dp[i][j] = 1  # 边界条件  跟上面注释掉的一个意思 不同表达
#             else:
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     return dp[n-1][m-1]
# 排列组合思想
# 要走到终点 从(0,0) -> (m-1, n-1) 共有 m-1 步向右走
# 同理  也有 n-1 步向下 结果都一样
# def solution(m, n):
#     import math
#     return int(math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1))
# 递归
def solution(m, n):
    def backtrack(i, j):
        if i == 0 or j == 0:
            return 1
        return backtrack(i-1, j) + backtrack(i, j-1)
    return backtrack(m-1, n-1)
print(solution(3, 2))