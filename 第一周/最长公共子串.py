# 子序列的输出不一定是连续的，子串的输出必须是连续的，注意两类题目的区别
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    # 构建dp表
    dp = [[0] * (n+1) for _ in range(m+1)] # m控制的行, n控制的列
    ans = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j]) # 若不加此句话，有些测试用例通不过
            else:
                dp[i][j] = 0
    #
    # return dp[-1][-1]
    return ans
print(lcs("12321", "32145"))