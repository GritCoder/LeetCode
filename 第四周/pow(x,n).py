# def solution(x, n):
#     res = 1.00000
#     if n >= 0:
#         for i in range(n):
#             res *= x
#     if n < 0:
#         for i in range(-n):
#             res *= 1.00000 / x
#     return res
# print(solution(2.00000,-2))

# 官方解法
def myPow(x: float, n: int) -> float:
    def quickMul(N):
        if N == 0:
            return 1.0
        y = quickMul(N // 2) # 取整除，本质是分治，看看是奇数次幂还是偶数次幂
        return y * y if N % 2 == 0 else y * y * x

    return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
print(myPow(2.00000, -2))
