# 数学推导法
'''
设将长度为 n 的绳子切为 a 段：n = n1+n2+....+na
本题等价于求max(n1xn2xn3...na)
由算术几何不等式得当n1=n2=n3....na时有最大值
设将绳子按照 x 长度等分为 a 段，即 n = ax 则乘积为y=x^a
a = n/x 代入y 然后求导可得当x=e时，取最大值，因此最接近3
'''
# def solution(n):
#     if n <= 3: # n=2 or n=3
#         return n-1
#     a, b = n // 3, n % 3  # // 是取整除(向下取整)
#     if b == 0:
#         return int(3**a)
#     if b == 1:
#         return int(3**(a-1) * 4)
#     if b == 2:
#         return int(3**a * 2)
# 动态规划
# 核心是理解 max(dp[i], max((i-j)*j, j*dp[i-j]))
# dp[i]表示维持原状不剪 (i-j)*j表示从j处剪一下以后不再剪 j*dp[i-j]表示j剪一下以后也剪
# def solution(n):
#     dp = [0 for _ in range(n+1)]
#     dp[2] = 1
#     for i in range(3, n+1): # 每一段绳子
#         for j in range(i): # 每一段绳子的剪法
#             dp[i] = max(dp[i], max((i-j)*j, j*dp[i-j]))
#     return dp[n]
# 动态规划优化版本
'''
我们发现任何大于 3 的数都可以拆分为数字 1，2，3的和
且它们对 3 的余数总是 0，1，2,因此我们可以仅用 dp[0]，dp[1]，dp[2] 
表示所有大于 3 的值，这样空间复杂度可降到 O(1) 时间复杂度为O(n)
此时状态方程的理解:三种情况(1)拆分成包含1的(2)拆分成包含2的(3)拆分成包含3的
拆分成1后，其余部分可能继续拆，也可能不拆(2,3也类似)，因此有max(dp[(i-1)%3], i-1)
关于1*max(dp[(i-1)%3], i-1)的理解:本质是把绳子看成两段，一段为1
另一段为max(dp[(i-1)%3], i-1)，然后返回的是这两段乘积即可
'''
# def solution(n):
#     # 初始状态
#     dp = [0, 1, 1]
#     for i in range(3, n+1):
#         dp[i%3] = max(1*max(dp[(i-1)%3], i-1), 2*max(dp[(i-2)%3], i-2),
#                       3*max(dp[(i-3)%3], i-3))
#     return dp[n%3]

# 暴力法(递归)
# 递归函数 f(n)=max(i*(n-i), i*f(n-i)) [其实各种方法本质上都是把绳子看作两段]
'''
@符号用做函数的修饰符，可以在模块或者类的定义层内对函数进行修饰
出现在函数定义的前一行，不允许和函数定义在同一行。一个修饰符就是一个函数，它将被修饰的函数作为参数
并返回修饰后的同名函数或其他可调用的东西（如果返回不是一个可调用的对象那么会报错）。
'''
from functools import lru_cache
@lru_cache(None)
# 亲测,方案(1)要比方案(2)高效的多!
def solution(n):
    # 执行严重超时，因为重复计算很多f(n)
    # 优化方案:(1)函数外加入@lru_cache(None)
    if n == 2:
        return 1
    # 初始化
    res = -1
    for i in range(1, n):
        res = max(res, max(i*(n-i), i*solution(n-i)))
    return res
# 优化方案:(2)记录f(n)是否计算过，见下面注释代码
# def solution(n):
#     f = [0 for _ in range(n+1)]
#     def cal(n):
#         if n == 2:
#             return 1
#         if f[n] != 0:# 说明已经计算过，直接返回计算结果
#             return f[n]
#         res = -1
#         for i in range(1, n):
#             res = max(res, max(i*(n-i), i*cal(n-i)))
#         return res
#     return cal(n)
print(solution(58))