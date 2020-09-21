# 暴力法
def solution(prices):
    if not prices:
        return 0
    n = len(prices)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, prices[j]-prices[i])
    return ans
# 一次遍历法
'''
假如计划在第 i 天卖出股票，那么最大利润的差值一定是在[0, i-1] 之间选最低点买入；所以遍历数组，依次求每个卖出时机的的最大差值，再从中取最大值。
在题目中，我们只要用一个变量记录一个历史最低价格 minprice
'''
def solution1(prices):
    minprice = int(1e9)
    ans = 0
    for price in prices:
        minprice = min(minprice, price)
        ans = max(ans, price - minprice)
        # if price < minprice:
        #     minprice = price
        # if ans < price - minprice:
        #     ans = price - minprice
    return ans if prices else 0