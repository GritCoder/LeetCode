# 动态规划
# def func(inputs):
#     dic = {0:-1}
#     sum, length = 0, len(inputs)
#     maxLen = 0
#     for i in range(length):
#         sum += inputs[i]
#         if sum in dic:
#             print(sum)
#             maxLen = max(maxLen, i-dic[sum])
#         else:
#             dic[sum] = i
#     return maxLen
# 暴力法
def func(inputs):
    length = len(inputs)
    maxLen = 0
    for i in range(length):
        sum = 0
        for j in range(i, length):
            sum += inputs[j]
            if sum == 0:
                maxLen = max(maxLen, j-i+1)
    return maxLen
print(func([-1,1,-1,1,-1]))