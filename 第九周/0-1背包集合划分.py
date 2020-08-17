# t = int(input().strip())
# n = int(input().strip())
# arrs = list(map(int, input().strip().split()))
'''
这个题是0-1背包问题的变种，首先来说对于每个数，我们只有两种选择，要么选，要么不选，而且选的话只能选择一次。
如果不选的话 那么d[i][j]的状态就跟前面的状态保持一致，即d[i][j] = d[i-1][j]，如果选的话，那就先判断一下目前包的剩余容量能不能放得下，如果放下，就选，即d[i][j] = arrs[i] + dp[i-1][j-arrs[i]]
最后我们取选与不选的最大值就OK了~
'''
def canPartition(arrs) -> bool:
    if not arrs:
        return False
    sum_ = sum(arrs)
    # 如果是奇数，肯定就不能划分了
    if sum_ % 2 != 0:
        return False
    target = sum_ // 2
    dp = [[0 for _ in range(target + 1)] for _ in range(len(arrs))]
    # 初始化，我们先把第一个数放进去，当然前提是能够放得下
    for i in range(target + 1):
        if arrs[0] <= i:
            dp[0][i] = arrs[0]
    # 联想一下dp表，第一行在初始化已经完成了，所以数组从1开始，注意包的容量并不受影响
    for i in range(1, len(arrs)):
        for j in range(target + 1):
            # 先不选
            dp[i][j] = dp[i - 1][j]
            # 如果能放得下，就选，然后更新d[i][j]为选和不选的最大值
            if arrs[i] <= j:
                dp[i][j] = max(dp[i][j], arrs[i] + dp[i - 1][j - arrs[i]])
    # 最后如果d[i][j] = target了 说明可以划分
    return dp[-1][-1] == target
