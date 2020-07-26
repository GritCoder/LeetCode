# 思路：对于温度列表中的每个元素 t[i]，需要找到最小的下标 j，使得 i < j 且 t[i] < t[j]
# 单调栈
def dailyTemperature(t):
    ans = [0] * len(t)
    stack = []
    for i in range(len(t)):
        tmp = t[i]
        while stack and tmp > t[stack[-1]]:
            pre = stack.pop()
            ans[pre] = i - pre # 核心语句
        stack.append(i) # 注意栈维护的是索引
    return ans
print(dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73]))