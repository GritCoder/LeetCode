# 动态规划
# def solution(inputs):
#     n = len(inputs)
#     dp = [[False] * n for _ in range(n)]
#     # print(dp)
#     ans = ""
#     # dp[i][j]表示从i->j子串是否是回文的
      # 子串的区间长度
#     for l in range(n):
          # 枚举子串的起始位置i，这样可以通过 j=i+l 得到子串的结束位置
#         for i in range(n):
#             j = i + l
#             if j >= n: # 结束条件
#                 break
#             if l == 0: # base = 1 dp表
#                 dp[i][j] = True
#             elif l == 1: # base = 2 dp表
#                 dp[i][j] = (inputs[i] == inputs[j])
#             else: # base >= 3 一般情况 从短往长扩展dp表
#                 dp[i][j] = (dp[i+1][j-1] and inputs[i] == inputs[j])
#             if dp[i][j] and l + 1 > len(ans): # 更新结果
#                 ans = inputs[i:j+1] # +1 是因为左闭右开
#     return ans
# 暴力法
def solution(inputs):
    n = len(inputs)
    res = ""
    for i in range(n):
        tmp = ""
        for j in range(i, n):
            tmp = tmp + inputs[j]
            temp = tmp[::-1] # 最简单的反转方式
            if tmp == temp:
                # 不能简单的用max，因为max得到的是长度，而不是串
                res = res if len(res) > len(temp) else temp
    return res
print(solution("1123212"))