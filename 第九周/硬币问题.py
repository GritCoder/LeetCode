# 拿硬币 桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。
# 一堆一堆的拿 彼此是独立的 本质上是贪心
def minCount(coins):
    # 求单堆硬币最小次数：(x+1)//2 加1是考虑到有些堆可能就一枚硬币
    cnt = 0
    for x in coins:
        cnt += (x + 1) // 2
    return cnt

# 动态规划
'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
'''
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # 基本思路就是求出每一种硬币的兑换次数，然后取最小就行了
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin] + 1) # dp[x] 表示不用这个硬币 dp[x-coin] 表示用这个硬币 然后次数+1
    return dp[amount] if dp[amount] != float('inf') else -1
# print(coinChange([1,2,5], 11))
# 硬币兑换，给你几种面值的硬币和一个硬币总数，求兑换方案个数
# 这里是不限次数的，因此属于完全背包问题(约束条件：每种物品的数量为无限个，你可以选择任意数量的物品。)
def waysToChange(n):
    dp = [0] * (n+1)
    dp[0] = 1
    mod = 10 ** 9 + 7
    coins = [25, 10, 5, 1]
    for coin in coins:
        for x in range(coin, n+1):
            dp[x] += dp[x-coin] # 思路很简单，分别求出四种硬币的方案，然后相加就行
    return dp[n] % mod
print(waysToChange(5))

