# 假设你正在爬楼梯，需要 n 阶你才能到达楼顶。每次只能爬一阶或者二阶 共多少种爬法
# 动态规划
# def climbStairs(n: int) -> int:
#     if n == 1 or n == 2:
#         return n
#     f = [0] * (n+1)
#     f[1] = 1
#     f[2] = 2
#     for i in range(3, n + 1):
#         f[i] = f[i - 1] + f[i - 2]
#     return f[n]
# 递归
import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def climbStairs(n: int) -> int:
    if n == 1 or n == 2:
        return n
    else:
        return climbStairs(n-1) + climbStairs(n-2)
print(climbStairs(10))

# 注: 实测很多次了, 递归 + lru_cache 的效率比动态规划还高