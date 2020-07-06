# 其实这个题有点类似于最长公共子串的味道
def solution(A, B):
    a, b = len(A), len(B)
    dp = [[0]*(a+1) for _ in range(b+1)]
    # print(dp)
    ans = 0
    # start = end = 0 # 初步尝试记录索引位置
    for i in range(1, a+1):
        for j in range(1, b+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j])
                # start = i
                # end = j
            else:
                dp[i][j] = 0

    # print(start, end)
    return ans
print(solution([1,2,3,2,1], [3,2,1,4,7]))