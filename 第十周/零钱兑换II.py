# 回溯+减枝
'''
        def change_recusion(amount, coins, res, start):

            for i in range(start, len(coins)):
                amount -= coins[i]
                if amount == 0:
                    res[0] += 1
                    return
                if amount < 0:
                    return
                change_recusion(amount, coins, res, i)
                # 这里是标准的回溯
                amount += coins[i]
        res = [0]
        coins.sort()
        change_recusion(amount, coins, res, 0)
        return 1 if amount == 0 else res[0]
'''
def solution1(amount, coins):
    ans = [0]
    def backtrack(coins, index, amount, ans):
        if amount == 0:
            ans[0] += 1
            return
        if amount < 0:
            return
        for i in range(index, len(coins)):
            backtrack(coins[i:], index, amount-coins[i], ans)
    backtrack(coins, 0, amount, ans)
    return ans[0]

def solution2(amount, coins):
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    return dp[amount]
print(solution2(10, [10]))