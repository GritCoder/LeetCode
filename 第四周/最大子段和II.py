# 给定 n 个整数，找出平均数最大且长度为 k 的子数组，并输出该最大平均数
def solution(arr, k):
    res = 0.0; tmp = 0.0
    # end = 0
    for i in range(len(arr)):
        if i < k: # 先加够k个数
            tmp += arr[i]
            res = tmp
            continue
        # 再往后加一个数，同时删除最前面一个数，保证长度不变
        tmp = tmp + arr[i] - arr[i-k]
        # 比较更新
        if tmp > res:
            res = tmp
            # end = i
    # print(end) # 注释部分记录了结束的索引，进而再结合k 就可以求出子段
    return res / k
print(solution([1,12,-5,-6,50,3], 4))


