# 思路跟丑数那个很类似，都是dp
# 核心思路：最小的丑数只可能出现在如dp[l2]的2倍、dp[l7]的7倍、dp[l13]的13倍和dp[l19]的19倍四者中间。
# 通过移动K个指针，就能保证生成的丑数是有序的。通过求到最小值来保证丑数数组有序排列。
# 编写一段程序来查找第n个超级丑数。超级丑数是指其所有质因数都是长度为k的质数列表primes中的正整数。
def solution(n, primes):
    # 返回结果的list，最后返回dp[-1]
    dp = [0] * n
    # 第一个丑数为 1
    dp[0] = 1
    # 质数列表的索引，用来求最小质数用的
    ks = [0] * len(primes)
    for i in range(1, n):
        dp[i] = min(x * dp[y] for x, y in zip(primes, ks))
        # 更新最小的那个质数对应的索引
        for j in range(len(primes)):
            if dp[i] == primes[j] * dp[ks[j]]:
                ks[j] += 1
    return dp[-1]
print(solution(12, [2,7,13,19]))
