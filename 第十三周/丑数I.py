# 判断一个数是否为丑数 所有丑数的题，有一个前提就是，1 是第一个丑数
def solution(n):
    # 特判 0
    if n < 1: return False
    # 如果一个数是丑数，不断除以 2 3 5 后一定为 1
    while n % 2 == 0: n //= 2
    while n % 3 == 0: n //= 3
    while n % 5 == 0: n //= 5
    return n == 1
print(solution(1))