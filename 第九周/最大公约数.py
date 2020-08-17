# 求两个数的最大公约数
def gcd(a, b):
    # a作为除数 要是大的那个数
    a, b = (a, b) if a > b else (b, a)
    # 辗转相除法求最大公约数
    while b:
        a, b = b, a % b
    return a
# 求多个数的最大公约数 基本思路，两个两个求
def solution(nums):
    while len(nums) > 1:
        cur = []
        for i in range(len(nums)-1):
            tmp = gcd(nums[i], nums[i+1])
            cur.append(tmp)
        nums = cur
    return nums
nums = [2,4,6,8,20]
print(solution(nums)[0])
# 最小公倍数
def lcm(a,b):
    return a * b // gcd(a, b)
print(lcm(2, 6))