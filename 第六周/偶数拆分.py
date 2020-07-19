import math
def is_prime(num):
    k = int(math.sqrt(num)) # 统一判断就行了  不用单独把 2 什么的拉出来考虑了 万能公式
    for i in range(2, k+1):
        if num % i == 0:
            return 0 # 0表示不是
    return 1

def solution(n):
    if n == 4:
        print(int(n/2),int(n/2))
    # 注意从3开始 步长为2 如果从2开始 步长为3 则会有逻辑错误
    for i in range(3, int(n/2)+1, 2):
        if is_prime(i) and is_prime(n-i):
            print(i, n-i)
solution(10)