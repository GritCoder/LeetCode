# 子序列的输出不一定是连续的，子串的输出必须是连续的，注意两类题目的区别
# 非递归解法
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    # 构建dp表
    dp = [[0] * (n+1) for _ in range(m+1)] # m控制的行, n控制的列
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
# 递归解法(倒着来算的,与非递归方法正好相反,不过提交到LeetCode测评超时(结果正确))
# import functools
# def lcs(str1, str2):
#     @functools.lru_cache(None) # 在递归函数前增加此方法(装饰器)，可以减缓超时现象
#     def dp(i, j):
#         if i == -1 or j == -1:
#             return 0
#         if str1[i] == str2[j]:
#             return dp(i-1, j-1) + 1
#         else:
#             return max(dp(i-1, j), dp(i, j-1))
#     return dp(len(str1)-1, len(str2)-1)
print(lcs("3145", "2345"))