# 这个版本里面，丑数定义变了 丑数是可以被 a 或 b 或 c 整除的正整数。
# 思路的话，dp会超时，用二分法
# 那么对于一个丑数X，我们能够确定它是第几个丑数吗？
# --答案显然是可以的，我们只需要计算X或者说[0...X]区间中包含了多少个丑数因子即可。
def gcd(a, b):
    # 注意 这里有个隐藏的条件，就是 a > b 注意一下，此题是满足了，因为后面有排序
    # 实测，再加上百度搜索证明，求最大公约数，a与b谁大谁小都一样，不影响结果
    return b if a % b == 0 else gcd(b, a % b)
def solution(n, a, b, c):
    a, b, c = sorted([a, b, c])
    lcm_ab = a * b // gcd(a, b)
    lcm_ac = a * c // gcd(a, c)
    lcm_bc = b * c // gcd(b, c)
    lcm_abc = lcm_ab * c // gcd(lcm_ab, c)
    if a == 1: return n
    # 区间按最小的质数算就行了，大的质数算，会超出真实个数，理解
    low, high = a, a * n
    while low <= high:
        mid = low + (high - low) // 2
        # 计算中间的 mid 是第几个丑数
        num = mid // a + mid // b + mid // c - mid // lcm_ab - mid // lcm_ac - mid // lcm_bc + mid // lcm_abc
        # 此处含义是，数字mid是第num个丑数
        if num == n:
            # 假如 mid = 10，min(a,b,c) = 5，那么在[10, 14]这个区间的数，都包含这么多个丑数因子，而我们只需要区间左端点，因此把多余的余数要减去
            # 明白理解此处的含义
            return mid - min(mid % a, mid % b, mid % c)
        elif num < n:
            low = mid + 1
        else:
            high = mid - 1
print(solution(1000000000,2,217983653,336916467))
# print(gcd(2,6))
