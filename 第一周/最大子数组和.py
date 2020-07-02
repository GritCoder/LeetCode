# 动态规划做法
# def sub_MaxArr(arr):
#     length = len(arr)
#     dp = [0] * length
#     dp[0] = arr[0]
#     res = dp[0]
#     for i in range(1, length):
#         dp[i] = max(dp[i-1]+arr[i], arr[i]) # 等价于 dp[i] = arr[i] if dp[i-1] < 0 else arr[i] + dp[i-1]
#         res = max(dp[i], res)
#     return res
# 暴力法
def sub_MaxArr(arr):
    length = len(arr)
    res = arr[0]
    # start = 0; end = 0
    for i in range(length):
        sum = 0
        for j in range(i, length):
            sum += arr[j]
            if sum > res:
                res = sum
                # start = i
                # end = j
    # print(start, end) # 注释掉的部分记录的是子段和的起始和结束的索引位置
    return res
print(sub_MaxArr([1,2,-1,0]))
